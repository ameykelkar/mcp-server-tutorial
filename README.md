# Demo MCP Server Tutorial 🚀

A demonstration Model Context Protocol (MCP) server that provides password generation and security analysis tools using the FastMCP framework.

## Overview

This MCP server showcases how to build custom tools that can be used by AI assistants and other MCP-compatible clients. It provides two main password-related functionalities:

- **Password Generation**: Create secure random passwords with customizable parameters
- **Password Scoring**: Analyze password strength with detailed feedback and scoring

## Features

### 🔑 Password Generator
- Configurable password length (minimum 4 characters)
- Optional symbol inclusion for enhanced security
- Uses secure random character selection from multiple character sets

### 📊 Password Strength Analyzer
- Comprehensive scoring system (0-10 scale)
- Multi-factor analysis including:
  - Length assessment
  - Character variety (lowercase, uppercase, digits, symbols)
  - Pattern detection (sequential, repetitive, common weak patterns)
  - Keyboard pattern recognition
- Detailed feedback with actionable recommendations
- Strength categorization (Very Weak to Very Strong)

## Requirements

- Python 3.13+
- FastMCP framework

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd mcp-server-tutorial
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install fastmcp>=2.10.5
```

## Usage

### Running the Server

Start the MCP server:
```bash
python server.py
```

The server will start and be ready to accept connections from MCP-compatible clients.

### Available Tools

#### `generate_password`
Generate a random secure password.

**Parameters:**
- `length` (int, optional): Password length, default is 12, minimum is 4
- `include_symbols` (bool, optional): Include special symbols, default is True

**Example:**
```python
# Generate a 16-character password with symbols
generate_password(length=16, include_symbols=True)

# Generate a 8-character password without symbols  
generate_password(length=8, include_symbols=False)
```

#### `score_password`
Analyze password strength and provide detailed feedback.

**Parameters:**
- `password` (str): The password to evaluate

**Returns:**
- `score`: Numeric score from 0-10
- `strength`: Categorical strength assessment
- `feedback`: List of detailed feedback messages
- `length`: Password length
- `character_types`: Breakdown of character types used

**Example:**
```python
score_password("MyStr0ngP@ssw0rd!")
# Returns detailed analysis with score, feedback, and recommendations
```

## Development

### Project Structure
```
mcp-server-tutorial/
├── server.py          # Main MCP server implementation
├── pyproject.toml     # Project configuration and dependencies
├── README.md          # This file
└── uv.lock           # Dependency lock file
```

### Extending the Server

To add new tools:

1. Define a new function decorated with `@mcp.tool`
2. Add proper type hints and docstrings
3. Implement your functionality
4. The tool will automatically be available to MCP clients

Example:
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
    return result
```

## Integration with AI Assistants

This MCP server can be integrated with various AI assistants and applications that support the Model Context Protocol, allowing them to:

- Generate secure passwords on demand
- Analyze password strength in real-time
- Provide security recommendations
- Assist with password policy compliance

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is provided as a tutorial example. Please check the license file for specific terms.

## Learn More

- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)
