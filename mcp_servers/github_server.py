from mcp.server.fastmcp import FastMCP

mcp = FastMCP("github-server")


@mcp.tool()
def generate_readme(
    startup_name: str,
    description: str
) -> str:

    return f"""
# {startup_name}

## Description

{description}

## Features

- Market Research
- Competitor Analysis
- Persona Generation
- Product Planning

## Architecture

Multi-Agent ADK System

## Deployment

Streamlit
"""


@mcp.tool()
def generate_repo_structure() -> str:

    return """
project/

agents/

tools/

ui/

outputs/

README.md

requirements.txt
"""


if __name__ == "__main__":
    mcp.run()