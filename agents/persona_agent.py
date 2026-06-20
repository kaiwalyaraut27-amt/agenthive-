from tools.gemini_client import generate_response
from tools.prompt_templates import PERSONA_PROMPT


class PersonaAgent:

    def run(self, idea):
        prompt = PERSONA_PROMPT.format(
            idea=idea
        )

        return generate_response(prompt)