# HOOPS AI MCP

A solution combining the HOOPS AI WebAPI server and MCP server for Claude Desktop integration.

## Structure

```
HOOPS_AI-MCP/
├── webapi/         # FastAPI-based REST API (HOOPS AI WebAPI)
└── mcp_server/     # MCP server for Claude Desktop integration
```

---

## 1. Clone the repository

```bash
git clone https://github.com/toshi-bata/HOOPS_AI-MCP.git
cd HOOPS_AI-MCP
```

---

## 2. WebAPI Server Setup

### Requirements

- Python 3.9 (recommended: Miniconda/Anaconda environment)
- A valid **HOOPS AI license key**
- HOOPS AI Python package (`hoops_ai_cpu` or `hoops_ai_gpu`) installed in your environment

### Install dependencies

Open a terminal, move into the `webapi` folder, and install:

```bash
cd webapi
pip install -r requirements.txt
```

> Install the `hoops_ai_cpu` or `hoops_ai_gpu` package separately according to your HOOPS AI distribution instructions.

### Configure environment variables

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

### Start the WebAPI server

Run the following from the `webapi/` directory using the Python executable from your HOOPS AI conda environment:

```bash
C:\Users\user_name\miniconda3\envs\hoops_ai_cpu\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8001
```

The API will be available at `http://127.0.0.1:8001`.  
Interactive docs (Swagger UI) are at `http://127.0.0.1:8001/docs`.

---

## 3. MCP Server Setup (Claude Desktop)

The MCP server connects Claude Desktop to the HOOPS AI WebAPI.

### Register the MCP server in Claude Desktop

1. Open **Claude Desktop**
2. Go to **Settings** → **Developer** → **Edit Config**
3. This opens `claude_desktop_config.json`. Add the following entry under `mcpServers`:

```json
{
  "mcpServers": {
    "hoops-ai": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "C:\\path\\to\\HOOPS_AI-MCP\\mcp_server",
        "server.py"
      ]
    }
  }
}
```

> Replace `C:\\path\\to\\HOOPS_AI-MCP` with the actual path where you cloned this repository.

4. Save the file and restart Claude Desktop.

### Available MCP tools

| Tool | Description |
|---|---|
| `open_cad_viewer` | Open a CAD file in the 3D viewer and return the viewer URL |
| `get_MFR_table_of_contents` | Get the MFR dataset summary |
| `get_MFR_labels_description` | List all MFR label IDs, names, and descriptions |
| `search_MFR_files` | Find CAD files that contain a given manufacturing feature |

---

## License

This project uses the **HOOPS AI** library. A valid HOOPS AI license is required to run the server.  
Contact [Tech Soft 3D](https://hoops.com/) for licensing information.
