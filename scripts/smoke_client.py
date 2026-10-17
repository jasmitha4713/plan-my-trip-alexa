import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

URL = "http://127.0.0.1:8000/mcp"


async def main():
    async with streamablehttp_client(URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            init = await session.initialize()
            print("Protocol version:", init.protocolVersion)
            print("Server name:", init.serverInfo.name)

            tools = await session.list_tools()
            print("Tools:", [t.name for t in tools.tools])

            result = await session.call_tool("ping", {"name": "Jasmitha"})
            print("Result:", result.content[0].text)


asyncio.run(main())