from mcp.server.fastmcp import FastMCP

# 1. Create the server. The name is what clients see.
mcp = FastMCP("plan-my-trip", host="127.0.0.1", port=8000)


# 2. Register a tool. The decorator tells MCP "this function is a tool".
#    The type hints (name: str) become the tool's input schema automatically.
@mcp.tool()
def ping(name: str = "traveller") -> dict:
    """Check that the PLAN MY TRIP MCP server is alive."""
    return {"message": f"Hello, {name}! The PLAN MY TRIP MCP server is alive."}


# 3. Start the server using Streamable HTTP (the transport the hackathon requires).
if __name__ == "__main__":
    mcp.run(transport="streamable-http")