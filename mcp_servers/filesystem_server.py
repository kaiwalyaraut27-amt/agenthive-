from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("filesystem-server")


@mcp.tool()
def save_report(filename: str, content: str) -> str:
    """
    Save a startup report.
    """

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    filepath = f"outputs/reports/{filename}"

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)

    return f"Saved: {filepath}"


@mcp.tool()
def read_report(filename: str) -> str:

    filepath = f"outputs/reports/{filename}"

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


@mcp.tool()
def list_reports() -> list:

    path = "outputs/reports"

    if not os.path.exists(path):
        return []

    return os.listdir(path)


if __name__ == "__main__":
    mcp.run()