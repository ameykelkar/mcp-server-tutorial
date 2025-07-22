import random
import string

from fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("Demo MCP Server 🚀")

@mcp.tool
def generate_password(length: int = 12, include_symbols: bool = True) -> str:
    """Generate a random password
    
    Args:
        length: Length of the password (default: 12)
        include_symbols: Whether to include symbols in the password (default: True)
        
    Returns:
        A randomly generated password
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    mcp.run() 