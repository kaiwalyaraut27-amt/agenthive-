import streamlit as st

from agents.orchestrator import Orchestrator
from ui.progress_tracker import ProgressTracker

st.set_page_config(
    page_title="AgentHive — Multi-Agent Startup Builder",
    page_icon="⬡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────────────────────────────────
# STYLE
# ──────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

    :root{
        --bg-void: #0B0B1A;
        --bg-surface: #15142B;
        --bg-surface-2: #1B1A38;
        --line: rgba(255,255,255,0.08);
        --violet: #7C5CFF;
        --violet-soft: rgba(124,92,255,0.16);
        --text-primary: #E8E6F5;
        --text-dim: rgba(232,230,245,0.58);
        --green: #3DDC97;
        --pink: #FF6B9D;
    }

    html, body, [class*="css"]{
        font-family: 'Inter', sans-serif;
    }

    .stApp{
        background:
            radial-gradient(circle at 18% -10%, rgba(124,92,255,0.22), transparent 45%),
            radial-gradient(circle at 100% 10%, rgba(61,216,151,0.10), transparent 40%),
            var(--bg-void);
        color: var(--text-primary);
    }

    /* Hide default chrome */
    #MainMenu, footer, header {visibility: hidden;}
    div[data-testid="stToolbar"] {visibility: hidden;}

    .block-container{
        padding-top: 2.6rem;
        max-width: 760px;
    }

    /* ── Hero ───────────────────────────────────────────── */
    .hive-eyebrow{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--violet);
        margin-bottom: 0.6rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .hive-eyebrow::before{
        content: "";
        width: 7px; height: 7px;
        background: var(--violet);
        border-radius: 1px;
        transform: rotate(45deg);
        box-shadow: 0 0 10px var(--violet);
    }

    .hive-title{
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 2.7rem;
        line-height: 1.05;
        letter-spacing: -0.01em;
        margin: 0;
        background: linear-gradient(120deg, #F4F2FF 30%, #B6A6FF 65%, #7C5CFF 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hive-subtitle{
        font-size: 1.02rem;
        color: var(--text-dim);
        margin-top: 0.55rem;
        margin-bottom: 2.1rem;
        max-width: 540px;
        line-height: 1.55;
    }

    /* ── Hive pipeline row (signature element) ─────────────── */
    .hive-row{
        display: flex;
        justify-content: space-between;
        gap: 6px;
        padding: 1.1rem 0.8rem 0.6rem;
        margin-bottom: 1.6rem;
        background: linear-gradient(180deg, rgba(255,255,255,0.025), transparent);
        border: 1px solid var(--line);
        border-radius: 16px;
    }
    .hive-cell{
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.35rem;
        min-width: 0;
    }
    .hive-hex{
        width: 100%;
        max-width: 42px;
        aspect-ratio: 1;
        transition: filter 0.4s ease;
    }
    .hive-hex polygon{
        transition: fill 0.5s ease, stroke 0.5s ease;
    }
    .hive-cell-active .hive-hex{
        animation: hivePulse 1.3s ease-in-out infinite;
        filter: drop-shadow(0 0 8px var(--cell-color));
    }
    .hive-cell-done .hive-hex{
        filter: drop-shadow(0 0 4px var(--cell-color));
    }
    @keyframes hivePulse{
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.72; transform: scale(1.07); }
    }
    .hive-cell-label{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.58rem;
        letter-spacing: 0.02em;
        text-align: center;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 100%;
    }

    .hive-status-line{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.82rem;
        color: var(--text-dim);
        display: flex;
        align-items: center;
        gap: 0.55rem;
        padding: 0.2rem 0 1.3rem 0.2rem;
    }
    .hive-status-dot{
        width: 7px; height: 7px;
        border-radius: 50%;
        background: var(--green);
        box-shadow: 0 0 8px var(--green);
        flex-shrink: 0;
        animation: dotBlink 1.1s ease-in-out infinite;
    }
    @keyframes dotBlink{
        0%, 100% { opacity: 1; }
        50% { opacity: 0.3; }
    }

    /* ── Input area ─────────────────────────────────────── */
    .stTextArea label, .stTextArea p {
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        color: var(--text-primary) !important;
    }
    .stTextArea textarea{
        background: var(--bg-surface) !important;
        border: 1px solid var(--line) !important;
        border-radius: 14px !important;
        color: var(--text-primary) !important;
        font-size: 0.95rem !important;
        padding: 1rem !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .stTextArea textarea:focus{
        border-color: var(--violet) !important;
        box-shadow: 0 0 0 3px var(--violet-soft) !important;
    }
    .stTextArea textarea::placeholder{
        color: rgba(232,230,245,0.32) !important;
    }

    .stButton button{
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        background: linear-gradient(120deg, #7C5CFF, #5C3CFF) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.7rem 1.6rem !important;
        box-shadow: 0 4px 24px rgba(124,92,255,0.35) !important;
        transition: transform 0.15s ease, box-shadow 0.15s ease !important;
        width: 100%;
        margin-top: 0.9rem;
    }
    .stButton button:hover{
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 28px rgba(124,92,255,0.5) !important;
    }
    .stButton button:active{
        transform: translateY(0) !important;
    }

    /* ── Section divider ───────────────────────────────────── */
    .hive-divider{
        display: flex;
        align-items: center;
        gap: 0.7rem;
        margin: 2.6rem 0 1.1rem;
    }
    .hive-divider-label{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--text-dim);
        white-space: nowrap;
    }
    .hive-divider-line{
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, var(--line), transparent);
    }

    /* ── Expander cards ─────────────────────────────────── */
    div[data-testid="stExpander"]{
        background: var(--bg-surface) !important;
        border: 1px solid var(--line) !important;
        border-radius: 14px !important;
        margin-bottom: 0.7rem;
        overflow: hidden;
    }
    div[data-testid="stExpander"] summary{
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.98rem !important;
        padding: 0.95rem 1.1rem !important;
    }
    div[data-testid="stExpander"] summary:hover{
        background: rgba(255,255,255,0.02) !important;
    }
    div[data-testid="stExpander"] div[data-testid="stExpanderDetails"]{
        padding: 0.2rem 1.25rem 1.25rem !important;
        color: var(--text-dim) !important;
        line-height: 1.6;
    }

    /* Per-agent left accent bars, matched via nth-of-type order */
    div[data-testid="stExpander"]:nth-of-type(1){ border-left: 3px solid #7C5CFF !important; }
    div[data-testid="stExpander"]:nth-of-type(2){ border-left: 3px solid #6C8CFF !important; }
    div[data-testid="stExpander"]:nth-of-type(3){ border-left: 3px solid #5CB8FF !important; }
    div[data-testid="stExpander"]:nth-of-type(4){ border-left: 3px solid #3DDC97 !important; }
    div[data-testid="stExpander"]:nth-of-type(5){ border-left: 3px solid #E8C547 !important; }
    div[data-testid="stExpander"]:nth-of-type(6){ border-left: 3px solid #FF6B9D !important; }
    div[data-testid="stExpander"]:nth-of-type(7){ border-left: 3px solid #FF6B9D !important; }
    div[data-testid="stExpander"]:nth-of-type(8){ border-left: 3px solid #FF8C5C !important; }

    /* ── Alerts (success / error) ──────────────────────────── */
    div[data-testid="stAlert"]{
        background: var(--bg-surface-2) !important;
        border: 1px solid var(--line) !important;
        border-radius: 12px !important;
        color: var(--text-primary) !important;
    }

    /* ── Report card ────────────────────────────────────── */
    .hive-report-card{
        background: linear-gradient(160deg, rgba(124,92,255,0.10), rgba(21,20,43,0.4));
        border: 1px solid rgba(124,92,255,0.3);
        border-radius: 16px;
        padding: 1.6rem 1.7rem;
        line-height: 1.65;
        color: var(--text-primary);
    }
    .hive-report-card h2, .hive-report-card h3{
        font-family: 'Space Grotesk', sans-serif !important;
        color: #F4F2FF;
    }

    /* ── MCP footer chips ───────────────────────────────── */
    .hive-mcp-row{
        display: flex;
        gap: 0.6rem;
        flex-wrap: wrap;
        margin-top: 0.4rem;
    }
    .hive-mcp-chip{
        display: flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(61,216,151,0.08);
        border: 1px solid rgba(61,216,151,0.3);
        border-radius: 999px;
        padding: 0.5rem 0.95rem;
        font-size: 0.85rem;
        color: var(--text-primary);
    }
    .hive-mcp-chip-dot{
        width: 6px; height: 6px;
        border-radius: 50%;
        background: var(--green);
        box-shadow: 0 0 6px var(--green);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────────────────
# HERO
# ──────────────────────────────────────────────────────────────────────────
st.markdown('<div class="hive-eyebrow">Multi-agent system · 7 agents · 1 pipeline</div>', unsafe_allow_html=True)
st.markdown('<h1 class="hive-title">AgentHive</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="hive-subtitle">Describe a startup idea and watch a hive of specialized '
    'agents research, critique, and architect it into a complete plan — '
    'security-checked, competitor-aware, and ready to build.</p>',
    unsafe_allow_html=True,
)

idea = st.text_area(
    "Your idea",
    placeholder="e.g. A marketplace that connects local farmers directly with restaurants for next-day produce delivery...",
    height=110,
    label_visibility="collapsed",
)

generate_clicked = st.button("⬡  Generate Startup Plan", use_container_width=True)

status_placeholder = st.empty()

# ──────────────────────────────────────────────────────────────────────────
# RUN
# ──────────────────────────────────────────────────────────────────────────
if generate_clicked:
    if not idea or not idea.strip():
        st.warning("Give the hive something to work with — describe your idea first.")
        st.stop()

    orchestrator = Orchestrator()
    tracker = ProgressTracker()
    tracker.bind(status_placeholder)

    tracker.update("Waking up the hive...")
    result = orchestrator.run(idea, tracker)

    if "error" in result:
        st.error(result["error"])
        st.stop()

    status_placeholder.markdown(
        '<div class="hive-status-line"><span class="hive-status-dot"></span>'
        'All agents finished. Plan ready below.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hive-divider">'
        '<span class="hive-divider-label">Agent Findings</span>'
        '<span class="hive-divider-line"></span></div>',
        unsafe_allow_html=True,
    )

    with st.expander("🛡️  Security — input safety & compliance", expanded=False):
        st.success(result["security"])

    with st.expander("🔍  Research — market signals", expanded=False):
        st.write(result["research"])

    with st.expander("⚔️  Competitors — landscape scan", expanded=False):
        st.write(result["competitors"])

    with st.expander("👥  Personas — who you're building for", expanded=False):
        st.write(result["personas"])

    with st.expander("📐  Product Plan V1 — first draft", expanded=False):
        st.write(result["product_v1"])

    with st.expander("🧠  Critic Feedback — what's weak", expanded=False):
        st.write(result["feedback"])

    with st.expander("✨  Improved Product Plan — V2", expanded=True):
        st.write(result["product_v2"])

    with st.expander("🏗️  Technical Architecture", expanded=False):
        st.write(result["architecture"])

    st.markdown(
        '<div class="hive-divider">'
        '<span class="hive-divider-label">Final Report</span>'
        '<span class="hive-divider-line"></span></div>',
        unsafe_allow_html=True,
    )

    st.markdown(f'<div class="hive-report-card">{result["report"]}</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="hive-divider">'
        '<span class="hive-divider-label">MCP Integrations</span>'
        '<span class="hive-divider-line"></span></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hive-mcp-row">'
        '<div class="hive-mcp-chip"><span class="hive-mcp-chip-dot"></span>Filesystem MCP saved startup report</div>'
        '<div class="hive-mcp-chip"><span class="hive-mcp-chip-dot"></span>GitHub MCP generated repository template</div>'
        '</div>',
        unsafe_allow_html=True,
    )