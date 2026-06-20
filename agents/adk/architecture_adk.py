from google.adk.agents import Agent


architecture_agent = Agent(
    name="ArchitectureAgent",

    model="gemini-2.5-flash",

    description="""
    Design system architecture.
    """,

    instruction="""
    Create:

    - Frontend

    - Backend

    - Database

    - AI Layer

    - Deployment Plan
    """
)