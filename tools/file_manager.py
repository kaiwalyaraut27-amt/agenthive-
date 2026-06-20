import os


def save_markdown(report):

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    filepath = "outputs/reports/startup_report.md"

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    return filepath