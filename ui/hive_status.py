"""
HiveStatus — renders 7 hexagon "cells", one per agent in the pipeline.
Cells light up sequentially as the orchestrator progresses, staying lit
once complete. This is the app's signature visual element.
"""

AGENTS = [
    {"key": "security", "label": "Security", "color": "#7C5CFF"},
    {"key": "research", "label": "Research", "color": "#6C8CFF"},
    {"key": "competitors", "label": "Competitors", "color": "#5CB8FF"},
    {"key": "personas", "label": "Personas", "color": "#3DDC97"},
    {"key": "product", "label": "Product", "color": "#E8C547"},
    {"key": "critic", "label": "Critic", "color": "#FF6B9D"},
    {"key": "architecture", "label": "Architecture", "color": "#FF8C5C"},
]

_HEX_POINTS = "50,3 93,26 93,74 50,97 7,74 7,26"


def _hex_cell(agent, state):
    """state: 'idle' | 'active' | 'done'"""
    color = agent["color"]
    label = agent["label"]

    if state == "idle":
        fill = "rgba(255,255,255,0.03)"
        stroke = "rgba(255,255,255,0.14)"
        text_color = "rgba(232,230,245,0.35)"
        extra_class = ""
    elif state == "active":
        fill = f"{color}33"
        stroke = color
        text_color = "#F4F2FF"
        extra_class = "hive-cell-active"
    else:  # done
        fill = f"{color}1F"
        stroke = color
        text_color = "#F4F2FF"
        extra_class = "hive-cell-done"

    return (
        f'<div class="hive-cell {extra_class}" style="--cell-color:{color};">'
        f'<svg viewBox="0 0 100 100" class="hive-hex">'
        f'<polygon points="{_HEX_POINTS}" fill="{fill}" stroke="{stroke}" stroke-width="2.5" />'
        f'</svg>'
        f'<span class="hive-cell-label" style="color:{text_color};">{label}</span>'
        f'</div>'
    )


def render_html(active_index: int) -> str:
    """active_index: -1 = nothing started, 0..6 = currently on that step (prior ones done), >=7 = all done"""
    cells = []
    for i, agent in enumerate(AGENTS):
        if active_index < 0:
            state = "idle"
        elif i < active_index:
            state = "done"
        elif i == active_index:
            state = "active" if active_index < len(AGENTS) else "done"
        else:
            state = "idle"
        cells.append(_hex_cell(agent, state))

    if active_index >= len(AGENTS):
        cells = []
        for agent in AGENTS:
            cells.append(_hex_cell(agent, "done"))

    return f'<div class="hive-row">{"".join(cells)}</div>'


class HiveStatus:
    """Bound to a Streamlit placeholder; call advance(i) to re-render at step i."""

    def __init__(self, placeholder):
        self._placeholder = placeholder
        self.render(-1)

    def render(self, active_index: int):
        self._placeholder.markdown(render_html(active_index), unsafe_allow_html=True)

    def advance(self, step_index: int):
        self.render(step_index)