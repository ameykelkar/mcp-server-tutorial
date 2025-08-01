import string
import re

from fastmcp import FastMCP
import secrets

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
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@mcp.tool
def score_password(password: str) -> dict:
    """Score password strength on a scale of 0-10
    
    Args:
        password: The password to evaluate
        
    Returns:
        A dictionary containing the score (0-10) and detailed feedback
    """
    if not password:
        return {"score": 0, "feedback": "Empty password"}
    
    score = 0
    feedback = []
    
    # Length scoring (0-3 points)
    length = len(password)
    if length < 6:
        score += 0
        feedback.append("❌ Too short (< 6 characters)")
    elif length < 8:
        score += 1
        feedback.append("⚠️ Short (6-7 characters)")
    elif length < 12:
        score += 2
        feedback.append("✅ Good length (8-11 characters)")
    else:
        score += 3
        feedback.append("✅ Excellent length (12+ characters)")
    
    # Character variety scoring (0-4 points)
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_symbol = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password))
    
    char_types = sum([has_lower, has_upper, has_digit, has_symbol])
    
    if char_types == 1:
        score += 0
        feedback.append("❌ Only one character type used")
    elif char_types == 2:
        score += 1
        feedback.append("⚠️ Two character types used")
    elif char_types == 3:
        score += 2
        feedback.append("✅ Three character types used")
    else:
        score += 4
        feedback.append("✅ All character types used (upper, lower, digits, symbols)")
    
    # Pattern analysis (0-2 points deduction)
    pattern_penalty = 0
    
    # Check for sequential characters (123, abc, etc.)
    if re.search(r'(012|123|234|345|456|567|678|789|890)', password.lower()):
        pattern_penalty += 1
        feedback.append("❌ Contains sequential numbers")
    
    if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
        pattern_penalty += 1
        feedback.append("❌ Contains sequential letters")
    
    # Check for repetitive characters (aaa, 111, etc.)
    if re.search(r'(.)\1{2,}', password):
        pattern_penalty += 1
        feedback.append("❌ Contains repetitive characters")
    
    # Check for common weak patterns
    common_patterns = ['password', '123456', 'qwerty', 'admin', 'login', 'welcome']
    if any(pattern in password.lower() for pattern in common_patterns):
        pattern_penalty += 2
        feedback.append("❌ Contains common weak patterns")
    
    # Keyboard patterns
    keyboard_patterns = ['qwerty', 'asdf', 'zxcv', '1234', 'abcd']
    if any(pattern in password.lower() for pattern in keyboard_patterns):
        pattern_penalty += 1
        feedback.append("❌ Contains keyboard patterns")
    
    score = max(0, score - pattern_penalty)
    
    # Bonus points for very long passwords
    if length >= 16:
        score += 1
        feedback.append("🌟 Bonus: Very long password")
    
    # Cap the score at 10
    score = min(10, score)
    
    # Generate overall assessment
    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"
    elif score <= 6:
        strength = "Fair"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return {
        "score": score,
        "strength": strength,
        "feedback": feedback,
        "length": length,
        "character_types": {
            "lowercase": has_lower,
            "uppercase": has_upper,
            "digits": has_digit,
            "symbols": has_symbol
        }
    }

if __name__ == "__main__":
    mcp.run() 
