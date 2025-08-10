"""
MCP server that exposes tools generated from an OpenAPI spec using FastMCP.

Spec used: Swagger Petstore OpenAPI 3.0
Docs: https://petstore3.swagger.io/api/v3/openapi.json
"""

from __future__ import annotations

import os
import httpx
from fastmcp import FastMCP


PETSTORE_OPENAPI_URL = os.environ.get(
    "PETSTORE_OPENAPI_URL",
    "https://petstore3.swagger.io/api/v3/openapi.json",
)

# The Petstore spec declares a server at "/api/v3". Provide absolute base URL for clarity.
PETSTORE_BASE_URL = os.environ.get(
    "PETSTORE_BASE_URL",
    "https://petstore3.swagger.io/api/v3",
)


def build_mcp_from_openapi() -> FastMCP:
    """Create a FastMCP server from the Petstore OpenAPI specification."""
    # Load OpenAPI spec
    openapi_spec = httpx.get(PETSTORE_OPENAPI_URL, timeout=30.0).json()

    # Create async client for the API
    client = httpx.AsyncClient(base_url=PETSTORE_BASE_URL)

    # Build MCP from OpenAPI
    mcp = FastMCP.from_openapi(
        openapi_spec=openapi_spec,
        client=client,
        name="Petstore OpenAPI MCP",
    )
    return mcp

# Expose a module-level MCP instance so installers can discover it
mcp = build_mcp_from_openapi()


if __name__ == "__main__":
    mcp.run()


