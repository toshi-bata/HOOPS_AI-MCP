# HOOPS AI WebAPI

A FastAPI-based REST API that exposes [HOOPS AI](https://hoops.com/) capabilities:

- **MFR (Manufacturing Feature Recognition)** — search CAD files by machining feature label
- **CAD Viewer** — upload or reference CAD files and open an interactive 3D viewer

---

## Requirements

- Python 3.9 (recommended: Miniconda/Anaconda environment)
- A valid **HOOPS AI license key**
- HOOPS AI Python package (`hoops_ai_cpu` or `hoops_ai_gpu`) installed in your environment

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/toshi-bata/HOOPS_AI-WebAPI.git
cd HOOPS_AI-WebAPI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> Install the `hoops_ai_cpu` or `hoops_ai_gpu` package separately according to your HOOPS AI distribution instructions.

### 4. Configure environment variables

Copy `.env.example` to `.env` and fill in your values:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Open `.env` and set each variable:

| Variable | Required | Description |
|---|---|---|
| `HOOPS_AI_LICENSE` | ✅ | Your HOOPS AI license key |
| `HOOPS_AI_NOTEBOOK_DIR` | ✅ | Absolute path to your HOOPS AI notebooks directory |
| `HOOPS_AI_MFR_FLOW_NAME` | ✅ | MFR flow name (dataset files are resolved relative to this) |
| `HOOPS_AI_CAD_SHARED_DIR` | optional | Shared folder for CAD files (defaults to `./uploads`) |
| `HOOPS_AI_MFR_LABELS_DESCRIPTION` | optional | Custom MFR label map (Python dict literal) |

> **Note:** `HOOPS_AI_LICENSE` is read **only** from the `.env` file, not from system environment variables.

Example `.env`:

```
HOOPS_AI_LICENSE=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
HOOPS_AI_NOTEBOOK_DIR=C:\hoops_ai\notebooks
HOOPS_AI_MFR_FLOW_NAME=cadsynth_1000
```

---

## Starting the server

Use the Python executable from your HOOPS AI conda environment:

```bash
C:\Users\user_name\miniconda3\envs\hoops_ai_cpu\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8001
```

For development with auto-reload:

```bash
C:\Users\user_name\miniconda3\envs\hoops_ai_cpu\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8001 --reload
```

The API will be available at `http://127.0.0.1:8001`.  
Interactive docs (Swagger UI) are at `http://127.0.0.1:8001/docs`.

---

## API Usage

### MFR — Search files by feature

Returns CAD file names that contain a given manufacturing feature.

```
GET /MFR/files/search?feature_name=<name>
```

**Example:**

```bash
curl.exe "http://127.0.0.1:8001/MFR/files/search?feature_name=through%20hole"
# Windows PowerShell
curl.exe "http://127.0.0.1:8001/MFR/files/search?feature_name=circular%20blind%20step"
```

**Response:**

```json
{
  "file_names": ["bracket_a.stp", "housing_b.stp"]
}
```

---

### MFR — List label descriptions

Returns all MFR label IDs with their names and descriptions.

```
GET /MFR/labels/description
```

**Example:**

```bash
curl.exe "http://127.0.0.1:8001/MFR/labels/description"
```

---

### MFR — Dataset table of contents

Returns a summary of the loaded MFR dataset.

```
GET /MFR/dataset/table-of-contents
```

**Example:**

```bash
curl.exe "http://127.0.0.1:8001/MFR/dataset/table-of-contents"
```

---

### CAD Viewer — Browser UI

Open the browser and navigate to:

```
http://127.0.0.1:8001/CAD/viewer
```

The page shows two forms:

1. **Upload CAD file** — choose a local file and click *Open viewer*
2. **CAD file path in shared folder** — enter a filename or path relative to the shared folder and click *Open viewer from path*

Both forms submit to the API and return a JSON response containing `viewer_url`. Copy that URL and open it in your browser to launch the interactive 3D viewer.

> The viewer runs on a **separate port** from the API server. Make sure that port is accessible (not blocked by a firewall).

### CAD Viewer — Upload via API

```bash
# Windows PowerShell
curl.exe -X POST "http://127.0.0.1:8001/CAD/viewer" `
         -F "file=@C:\path\to\model.stp"
```

**Response:**

```json
{
  "viewer_url": "http://127.0.0.1:<viewer_port>/index.html"
}
```

Open the returned `viewer_url` in your browser to view the model.

### CAD Viewer — Open by shared path

> This endpoint is used internally by the browser UI form and is not listed in the Swagger docs.

```bash
# Windows PowerShell
curl.exe -X POST "http://127.0.0.1:8001/CAD/viewer/from-path" `
         -d "cad_file_path=model.stp"
```

The path can be a filename relative to the shared folder (`HOOPS_AI_CAD_SHARED_DIR`) or an absolute path within it.

**Response:**

```json
{
  "viewer_url": "http://127.0.0.1:<viewer_port>/index.html"
}
```

Open the returned `viewer_url` in your browser to view the model.

---

## Running tests

```bash
python -m unittest discover -s tests
```

---

## License

This project uses the **HOOPS AI** library. A valid HOOPS AI license is required to run the server.  
Contact [Tech Soft 3D](https://hoops.com/) for licensing information.
