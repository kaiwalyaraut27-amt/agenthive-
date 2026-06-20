from tools.file_manager import save_markdown


class MCPManager:

    def save_startup_report(
        self,
        report
    ):

        return save_markdown(report)