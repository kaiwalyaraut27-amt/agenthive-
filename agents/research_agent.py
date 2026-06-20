from tools.gemini_client import generate_response
from tools.prompt_templates import RESEARCH_PROMPT


class ResearchAgent:

    def run(self, idea):
        prompt = RESEARCH_PROMPT.format(
            idea=idea
        )

        return generate_response(prompt)