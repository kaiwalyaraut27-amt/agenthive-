from google.adk.agents import Agent


product_agent = Agent(
    name="ProductAgent",

    model="gemini-2.5-flash",

    description="""
    Generate PRD and MVP strategy.
    """,

    instruction="""
    Create:

    1. Product Vision

    2. MVP Features

    3. User Stories

    4. Monetization Strategy
    """
)