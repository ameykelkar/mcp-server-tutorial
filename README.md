## MCP Server Tutorial 🚀

A tutorial project demonstrating how to build Model Context Protocol (MCP) servers using FastMCP. This repo contains three example servers:

- Demo password tools (`server.py`)
- Employee API tools via a REST backend (`server_api.py`)
- OpenAPI-generated tools for the Petstore API (`server_openapi.py`)

## What is MCP?

The Model Context Protocol (MCP) is a standard that enables AI assistants to securely connect to external data sources and tools. These examples show different ways to build MCP servers that assistants can use.

## Prerequisites

- Python 3.13 or higher
- `uv` package manager (recommended) or pip

## Installation

### Using uv (recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp-server-tutorial
```

2. Install dependencies:
```bash
uv sync
```

### Using pip

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp-server-tutorial
```

2. Create a virtual environment and install deps:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install 'fastmcp>=2.10.5' 'httpx>=0.25.0'
```

## Usage

### 1) Demo Password Tools — `server.py`

Run the server:
```bash
uv run server.py
# or
python server.py
```

Available tools:
- `generate_password(length: int = 12, include_symbols: bool = True) -> str`
  - Generates a random password. Minimum length is 4.
- `score_password(password: str) -> dict`
  - Returns `score` (0–10), `strength`, `feedback` list, `length`, and `character_types` details.

Examples:
```python
generate_password(length=16, include_symbols=True)
score_password("MySecureP@ssw0rd!")
```

### 2) Employee API Tools — `server_api.py`

Backed by `https://dummy.restapiexample.com/api/v1`.

Run the server:
```bash
uv run server_api.py
# or
python server_api.py
```

Available tools:
- `get_all_employees() -> Dict[str, Any]`
- `get_employee_by_id(employee_id: int) -> Dict[str, Any]`
- `filter_employees_by_age(min_age: Optional[int] = None, max_age: Optional[int] = None) -> Dict[str, Any]`
- `filter_employees_by_salary(min_salary: Optional[int] = None, max_salary: Optional[int] = None) -> Dict[str, Any]`
- `search_employees_by_name(name_query: str) -> Dict[str, Any]`
- `get_employee_statistics() -> Dict[str, Any]`

Notes:
- The external API can be rate-limited or flaky; errors are returned as `{ "error": "..." }`.

### 3) Petstore OpenAPI Tools — `server_openapi.py`

Generates tools dynamically from the Petstore OpenAPI spec.

Environment variables (optional):
- `PETSTORE_OPENAPI_URL` (default: `https://petstore3.swagger.io/api/v3/openapi.json`)
- `PETSTORE_BASE_URL` (default: `https://petstore3.swagger.io/api/v3`)

OpenAPI specification:
`https://petstore3.swagger.io/api/v3/openapi.json`

Run the server:
```bash
uv run server_openapi.py
# or
python server_openapi.py
```

About the tools:
- Tools are generated directly from the OpenAPI spec and mirror API operations
  (e.g., pet, store, and user endpoints in the Petstore API).
- Requires internet access to fetch the OpenAPI spec and call the API.

### Connecting to AI Assistants

Configure your MCP-compatible client (e.g., Claude Desktop) to connect to the server you are running. Refer to your client’s documentation for how to register MCP servers.

## Development

### Project structure

```
mcp-server-tutorial/
├── server.py            # Demo password tools
├── server_api.py        # Employee API tools (dummy.restapiexample.com)
├── server_openapi.py    # OpenAPI-generated tools (Petstore)
├── README.md            # This file
├── pyproject.toml       # Project configuration
└── uv.lock              # Dependency lock file
```

### Adding new tools

For hand-written tools (e.g., in `server.py` or `server_api.py`):
1. Define a function with the `@mcp.tool` decorator
2. Add proper type hints and a concise docstring
3. Implement your logic; tools are auto-exposed to MCP clients

```python
@mcp.tool
def my_new_tool(param: str) -> str:
    return "result"
```

For OpenAPI-based servers, adjust the OpenAPI source URL and base URL, then rebuild the server with `FastMCP.from_openapi` as shown in `server_openapi.py`.

## Dependencies

- `fastmcp>=2.10.5`
- `httpx>=0.25.0`

## Troubleshooting

- **Server won’t start**: Verify Python 3.13+, dependencies installed, and network availability (for API/OpenAPI servers).
- **External API errors**: The Employee and Petstore servers depend on public APIs that may rate-limit or return intermittent errors. Check the returned `{ "error": "..." }` message.
- **Client can’t connect**: Confirm the server process is running and the MCP client is correctly configured.

---

Happy coding! 🎉
