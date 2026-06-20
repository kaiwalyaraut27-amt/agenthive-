from tools.gemini_client import generate_response
from tools.prompt_templates import COMPETITOR_PROMPT


class CompetitorAgent:

    def run(self, idea):
        prompt = COMPETITOR_PROMPT.format(
            idea=idea
        )

        return generate_response(prompt)