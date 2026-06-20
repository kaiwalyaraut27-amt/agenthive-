from google.adk.agents import Agent


research_agent = Agent(
    name="ResearchAgent",

    model="gemini-2.5-flash",

    description="""
    Research startup markets and opportunities.
    """,

    instruction="""
    You are a startup market researcher.

    Analyze startup ideas.

    Provide:

    1. Market Opportunity

    2. Industry Trends

    3. Risks

    4. Opportunities
    """
)