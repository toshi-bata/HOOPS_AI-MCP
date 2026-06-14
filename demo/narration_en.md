# HOOPS AI MCP — Demo Narration (English)

---

## Slide 1 — Title

Today I'd like to introduce HOOPS AI MCP — a platform for intelligent CAD data analysis. It delivers four core capabilities: CAD Viewer, B-Rep Analysis, Manufacturing Feature Recognition, and Shape Similarity Search. These are accessible through two interfaces: a REST API built with FastAPI, and an MCP Server that lets Claude Desktop control everything using natural language.

---

## Slide 2 — Architecture

The system is organized in four layers. At the foundation is HOOPS AI by Tech Soft 3D, which handles CAD file loading, geometry analysis, and ML inference. On top of that sits the FastAPI WebAPI, which exposes those capabilities as REST endpoints. The MCP Server wraps the WebAPI and acts as a bridge, allowing Claude Desktop to invoke tools using natural language. Finally, Claude Desktop operates as the AI agent — autonomously calling MCP tools to carry out end-to-end CAD analysis tasks.

---

## Slide 3 — Features

Let me walk through the four features. First, the CAD Viewer renders 30+ formats — including STEP, SolidWorks, CATIA, and NX — interactively in the browser. B-Rep Analysis generates face adjacency graphs and extracts face and edge attributes such as type, area, length, and dihedral angle. MFR uses a trained ML model to automatically recognize 24 machining feature types like holes, slots, and pockets, with results visualized as color overlays in the viewer. Finally, CAD Similarity Search converts shapes into feature vectors with HOOPS Embeddings and retrieves similar parts at high speed using a FAISS index.

---

## Slide 4 — WebAPI Endpoints

The WebAPI organizes endpoints by feature. It offers 11 endpoints in total: CAD Viewer launch and termination; B-Rep face adjacency graph generation and attribute extraction; MFR file search, thumbnail retrieval, label listing, inference execution, and viewer colorization; and shape similarity search. All endpoints are immediately testable through the built-in Swagger UI.

---

## Slide 5 — MCP Tools

MCP Tools are the toolset available to Claude Desktop. We provide 11 tools mapped to each WebAPI feature. Claude can launch the viewer, recognize machining features, or search for similar shapes — all from natural language instructions alone. The key advantage is that engineers can conduct interactive CAD analysis without writing any code.

---

## Slide 6 — Summary

To summarize: HOOPS AI MCP delivers CAD intelligence through two complementary approaches — a REST API and AI agent integration. B-Rep analysis and manufacturing feature recognition provide deep understanding of CAD data, while the combination of HOOPS Embeddings and FAISS has demonstrated similarity search accuracy of 0.99 and above. We invite you to explore the new possibilities this platform brings to CAD data utilization.
