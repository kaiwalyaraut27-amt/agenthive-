from google.adk.agents import Agent


critic_agent = Agent(
    name="CriticAgent",

    model="gemini-2.5-flash",

    description="""
    Critique startup plans.
    """,

    instruction="""
    Review startup plans.

    Identify:

    - Risks

    - Weak assumptions

    - Missing features

    - Improvements
    """
)