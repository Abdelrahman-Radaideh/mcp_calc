import doctest
import os
from fastmcp import FastMCP

mcp = FastMCP(name = 'Calculator')

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    args: a (float): The first number.
    | | b (float): The second number.

    returns: float: The product of the two numbers.
    """
    return a * b
@mcp.tool(name = 'add',
          description = 'Add two numbers.',
          tags = {"Math" , "arithmatic"}) # letting the agent access this tool
def add(a: float, b: float) -> float:
    """Add two numbers.
    args: a (float): The first number.
    | | b (float): The second number.
    returns: float: The sum of the two numbers.

    """
    return a + b

@mcp.tool(name = 'subtract',
          description = 'Subtract two numbers.',
          tags = {"Math" , "arithmatic"})
def subtract(a: float, b: float) -> float:
    """Subtract two numbers.
    args: a (float): The first number.
    | | b (float): The second number.
    returns: float: The sum of the two numbers.
    """
    return a - b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers.
    args: a (float): The first number.
    | | b (float): The second number.
    returns: float: The quotient of the two numbers.
    """
    if b == 0:
        raise ValueError('Divide by zero')
    return a / b

if __name__ == '__main__':

    #mcp.run()#STDIO by defualt
    port = int(os.environ.get("PORT", 8002))
    mcp.run(transport="http", host="0.0.0.0", port=port)
