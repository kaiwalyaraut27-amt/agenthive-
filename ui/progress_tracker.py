"""
ProgressTracker — drives the live status line in the UI.

Call .bind(status_placeholder) once you have the rendered placeholder,
then .update(message) at each pipeline step. Falls back to a no-op print
if unbound, so the orchestrator never needs to know whether a UI is attached.
"""


class ProgressTracker:
    def __init__(self):
        self._status_placeholder = None

    def bind(self, status_placeholder):
        self._status_placeholder = status_placeholder

    def update(self, message: str):
        if self._status_placeholder is not None:
            self._status_placeholder.markdown(
                f'<div class="hive-status-line">'
                f'<span class="hive-status-dot"></span>{message}</div>',
                unsafe_allow_html=True,
            )
        else:
            print(f"[AgentHive] {message}")