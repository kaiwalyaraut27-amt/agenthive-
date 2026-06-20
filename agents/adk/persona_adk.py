from google.adk.agents import Agent


persona_agent = Agent(
    name="PersonaAgent",

    model="gemini-2.5-flash",

    description="""
    Create customer personas.
    """,

    instruction="""
    Create detailed customer personas.

    Include:

    - Demographics

    - Pain Points

    - Goals

    - Behaviors
    """
)