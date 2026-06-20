from agents.research_agent import ResearchAgent
from agents.competitor_agent import CompetitorAgent
from agents.persona_agent import PersonaAgent
from agents.product_agent import ProductAgent
from agents.critic_agent import CriticAgent
from agents.architecture_agent import ArchitectureAgent
from agents.security_agent import SecurityAgent
from tools.report_generator import generate_report
from tools.file_manager import save_markdown

class Orchestrator:

    def __init__(self):

        self.research_agent = ResearchAgent()

        self.competitor_agent = CompetitorAgent()

        self.persona_agent = PersonaAgent()

        self.product_agent = ProductAgent()

        self.critic_agent = CriticAgent()

        self.architecture_agent = ArchitectureAgent()

        self.security_agent = SecurityAgent()

    def run(self, idea, tracker=None):

        is_safe, message = self.security_agent.run(idea)
    
        if not is_safe: raise ValueError(message)

        if tracker:

            tracker.update(
                "Research Agent Running..."
            )

        research = self.research_agent.run(idea)

        if tracker:

            tracker.update(
                "Research Agent Running..."
            )

        competitors = self.competitor_agent.run(idea)
    
        if tracker:

            tracker.update(
                "Research Agent Running..."
            )
        personas = self.persona_agent.run(idea)

        if tracker:

            tracker.update(
                "Research Agent Running..."
            )

        product = self.product_agent.run(
            research,
            competitors,
            personas
        )

        if tracker:

           tracker.update(
            "Research Agent Running..."
    )

        feedback = self.critic_agent.run(product)

        if tracker:

            tracker.update(
                "Research Agent Running..."
            )

        improved_product = self.product_agent.improve_plan(product, feedback)

        if tracker:

                tracker.update(
                    "Research Agent Running..."
                )

        architecture = self.architecture_agent.run(idea, product)

        if tracker:

            tracker.update(
                "Generating Final Report..."
            )

        report = generate_report({

            "research": research,

            "competitors": competitors,

            "personas": personas,

            "product_v2": improved_product,

            "architecture": architecture
        })

        report_path: str = save_markdown(report)

        return {

            "research": research,

            "competitors": competitors,

            "personas": personas,

            "product_v1": product,

            "feedback": feedback,

            "product_v2": improved_product,

            "architecture": architecture,

            "security": message,

            "report": report,

            "report_path": report_path
        }