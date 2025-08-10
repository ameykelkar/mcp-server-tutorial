import httpx
from typing import Optional, List, Dict, Any
from fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("Employee API MCP Server")

# Base API URL
API_BASE_URL = "https://dummy.restapiexample.com/api/v1"

@mcp.tool
async def get_all_employees() -> Dict[str, Any]:
    """Fetch all employees from the API
    
    Returns:
        Dictionary containing all employee data from the API
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{API_BASE_URL}/employees")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error occurred: {e}"}
        except Exception as e:
            return {"error": f"An error occurred: {e}"}

@mcp.tool
async def get_employee_by_id(employee_id: int) -> Dict[str, Any]:
    """Get a specific employee by their ID
    
    Args:
        employee_id: The ID of the employee to fetch
        
    Returns:
        Dictionary containing the employee data
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{API_BASE_URL}/employee/{employee_id}")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error occurred: {e}"}
        except Exception as e:
            return {"error": f"An error occurred: {e}"}

@mcp.tool
async def filter_employees_by_age(min_age: Optional[int] = None, max_age: Optional[int] = None) -> Dict[str, Any]:
    """Filter employees by age range
    
    Args:
        min_age: Minimum age (inclusive). If not provided, no minimum limit
        max_age: Maximum age (inclusive). If not provided, no maximum limit
        
    Returns:
        Dictionary containing filtered employee data
    """
    # First get all employees
    all_employees_response = await get_all_employees()
    
    if "error" in all_employees_response:
        return all_employees_response
    
    if all_employees_response.get("status") != "success":
        return {"error": "Failed to fetch employee data"}
    
    employees = all_employees_response.get("data", [])
    filtered_employees = []
    
    for employee in employees:
        age = employee.get("employee_age", 0)
        if min_age is not None and age < min_age:
            continue
        if max_age is not None and age > max_age:
            continue
        filtered_employees.append(employee)
    
    return {
        "status": "success",
        "data": filtered_employees,
        "message": f"Found {len(filtered_employees)} employees matching age criteria",
        "filter_criteria": {
            "min_age": min_age,
            "max_age": max_age
        }
    }

@mcp.tool
async def filter_employees_by_salary(min_salary: Optional[int] = None, max_salary: Optional[int] = None) -> Dict[str, Any]:
    """Filter employees by salary range
    
    Args:
        min_salary: Minimum salary (inclusive). If not provided, no minimum limit
        max_salary: Maximum salary (inclusive). If not provided, no maximum limit
        
    Returns:
        Dictionary containing filtered employee data
    """
    # First get all employees
    all_employees_response = await get_all_employees()
    
    if "error" in all_employees_response:
        return all_employees_response
    
    if all_employees_response.get("status") != "success":
        return {"error": "Failed to fetch employee data"}
    
    employees = all_employees_response.get("data", [])
    filtered_employees = []
    
    for employee in employees:
        salary = employee.get("employee_salary", 0)
        if min_salary is not None and salary < min_salary:
            continue
        if max_salary is not None and salary > max_salary:
            continue
        filtered_employees.append(employee)
    
    return {
        "status": "success",
        "data": filtered_employees,
        "message": f"Found {len(filtered_employees)} employees matching salary criteria",
        "filter_criteria": {
            "min_salary": min_salary,
            "max_salary": max_salary
        }
    }

@mcp.tool
async def search_employees_by_name(name_query: str) -> Dict[str, Any]:
    """Search for employees by name (case-insensitive partial match)
    
    Args:
        name_query: Name or partial name to search for
        
    Returns:
        Dictionary containing matching employee data
    """
    # First get all employees
    all_employees_response = await get_all_employees()
    
    if "error" in all_employees_response:
        return all_employees_response
    
    if all_employees_response.get("status") != "success":
        return {"error": "Failed to fetch employee data"}
    
    employees = all_employees_response.get("data", [])
    matching_employees = []
    
    name_query_lower = name_query.lower()
    
    for employee in employees:
        employee_name = employee.get("employee_name", "").lower()
        if name_query_lower in employee_name:
            matching_employees.append(employee)
    
    return {
        "status": "success",
        "data": matching_employees,
        "message": f"Found {len(matching_employees)} employees matching name query '{name_query}'",
        "search_query": name_query
    }

@mcp.tool
async def get_employee_statistics() -> Dict[str, Any]:
    """Get statistical information about all employees
    
    Returns:
        Dictionary containing employee statistics (average age, salary, etc.)
    """
    # First get all employees
    all_employees_response = await get_all_employees()
    
    if "error" in all_employees_response:
        return all_employees_response
    
    if all_employees_response.get("status") != "success":
        return {"error": "Failed to fetch employee data"}
    
    employees = all_employees_response.get("data", [])
    
    if not employees:
        return {"error": "No employee data available"}
    
    # Calculate statistics
    total_employees = len(employees)
    ages = [emp.get("employee_age", 0) for emp in employees]
    salaries = [emp.get("employee_salary", 0) for emp in employees]
    
    avg_age = sum(ages) / len(ages) if ages else 0
    avg_salary = sum(salaries) / len(salaries) if salaries else 0
    min_age = min(ages) if ages else 0
    max_age = max(ages) if ages else 0
    min_salary = min(salaries) if salaries else 0
    max_salary = max(salaries) if salaries else 0
    
    return {
        "status": "success",
        "statistics": {
            "total_employees": total_employees,
            "age_stats": {
                "average": round(avg_age, 2),
                "minimum": min_age,
                "maximum": max_age
            },
            "salary_stats": {
                "average": round(avg_salary, 2),
                "minimum": min_salary,
                "maximum": max_salary
            }
        },
        "message": "Employee statistics calculated successfully"
    }

if __name__ == "__main__":
    mcp.run()




