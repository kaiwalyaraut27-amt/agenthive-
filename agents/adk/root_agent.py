from google.adk.agents import Agent

from agents.adk.research_adk import research_agent
from agents.adk.competitor_adk import competitor_agent
from agents.adk.persona_adk import persona_agent
from agents.adk.product_adk import product_agent
from agents.adk.critic_adk import critic_agent
from agents.adk.architecture_adk import architecture_agent


root_agent = Agent(
    name="AgentHiveRoot",

    model="gemini-1.5-flash",

    description="""
    Startup-building multi-agent system.
    """,

    instruction="""
    Coordinate startup planning tasks.
    """,

    sub_agents=[

        research_agent,

        competitor_agent,

        persona_agent,

        product_agent,

        critic_agent,

        architecture_agent
    ]
)
