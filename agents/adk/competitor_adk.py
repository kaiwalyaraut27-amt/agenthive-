from google.adk.agents import Agent


competitor_agent = Agent(
    name="CompetitorAgent",

    model="gemini-2.5-flash",

    description="""
    Analyze competitors.
    """,

    instruction="""
    Analyze competitors.

    Provide:

    1. Competitors

    2. Strengths

    3. Weaknesses
    """
)