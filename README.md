# MCP Server Tutorial 🚀

A tutorial project demonstrating how to build a Model Context Protocol (MCP) server using FastMCP. This server provides password-related tools for generating and evaluating password strength.

## What is MCP?

The Model Context Protocol (MCP) is a standard that enables AI assistants to securely connect to external data sources and tools. This tutorial shows how to create your own MCP server that AI assistants can use to extend their capabilities.

## Features

This MCP server provides two main tools:

- **🔐 Password Generation**: Create secure random passwords with customizable length and character sets
- **📊 Password Scoring**: Evaluate password strength with detailed feedback and security recommendations

## Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended) or pip

## Installation

### Using uv (Recommended)

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

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastmcp>=2.10.5
```

## Usage

### Running the Server

Start the MCP server:

```bash
# Using uv
uv run server.py

# Using python directly
python server.py
```

The server will start and be ready to accept connections from MCP-compatible clients.

### Connecting to AI Assistants

To use this MCP server with AI assistants like Claude Desktop, you'll need to configure the client to connect to your server. Refer to the specific documentation for your AI assistant on how to add MCP servers.

## Available Tools

### 1. Generate Password

Generate a secure random password with customizable options.

**Parameters:**
- `length` (int, optional): Length of the password (default: 12, minimum: 4)
- `include_symbols` (bool, optional): Whether to include symbols (default: True)

**Example:**
```python
# Generate a 16-character password with symbols
generate_password(length=16, include_symbols=True)

# Generate a 12-character password without symbols
generate_password(length=12, include_symbols=False)
```

### 2. Score Password

Evaluate password strength and get detailed security feedback.

**Parameters:**
- `password` (str): The password to evaluate

**Returns:**
- `score` (int): Strength score from 0-10
- `strength` (str): Overall strength assessment
- `feedback` (list): Detailed recommendations
- `length` (int): Password length
- `character_types` (dict): Analysis of character usage

**Scoring Criteria:**
- **Length (0-3 points)**: Longer passwords score higher
- **Character Variety (0-4 points)**: Using different character types improves score
- **Pattern Analysis**: Deductions for weak patterns, sequential characters, repetition
- **Bonus Points**: Extra points for very long passwords (16+ characters)

**Example:**
```python
score_password("MySecureP@ssw0rd!")
# Returns detailed analysis with score, strength level, and feedback
```

## Development

### Project Structure

```
mcp-server-tutorial/
├── server.py          # Main MCP server implementation
├── pyproject.toml     # Project configuration
├── README.md         # This file
└── uv.lock          # Dependency lock file
```

### Adding New Tools

To add new tools to the MCP server:

1. Define a function with the `@mcp.tool` decorator
2. Add proper type hints and docstrings
3. Implement your tool logic
4. The tool will automatically be available to MCP clients

**Example:**
```python
@mcp.tool
def my_new_tool(param: str) -> str:
    """Description of what this tool does
    
    Args:
        param: Description of the parameter
        
    Returns:
        Description of the return value
    """
    # Your implementation here
    return "result"
```

## Dependencies

- **FastMCP**: A fast and simple framework for building MCP servers
- **Python Standard Library**: Uses `random`, `string`, and `re` modules

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is for educational purposes. Please refer to the repository license for usage terms.

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [Password Security Best Practices](https://owasp.org/www-project-cheat-sheets/cheatsheets/Password_Storage_Cheat_Sheet.html)

## Troubleshooting

### Common Issues

**Server won't start:**
- Ensure Python 3.13+ is installed
- Check that all dependencies are installed
- Verify no other service is using the same port

**AI assistant can't connect:**
- Confirm the server is running
- Check the connection configuration in your AI assistant
- Ensure firewall settings allow the connection

**Tool not working as expected:**
- Check the function parameters and types
- Review the server logs for error messages
- Ensure input validation requirements are met

---

Happy coding! 🎉
