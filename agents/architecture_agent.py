from tools.gemini_client import generate_response


ARCHITECTURE_PROMPT = """
You are a Senior Software Architect.

Startup Idea:

{idea}

Product Plan:

{product}

Create a technical architecture.

Include:

1. Frontend
2. Backend
3. Database
4. AI Layer
5. Deployment
6. Scalability Considerations

Provide detailed explanations.
"""


class ArchitectureAgent:

    def run(self, idea, product):

        prompt = ARCHITECTURE_PROMPT.format(
            idea=idea,
            product=product
        )

        return generate_response(prompt)