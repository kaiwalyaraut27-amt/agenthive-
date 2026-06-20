from tools.gemini_client import generate_response

CRITIC_PROMPT = """
You are a startup advisor.

Review the following startup product plan.

Identify:

1. Missing features
2. Business risks
3. Weak assumptions
4. Suggested improvements

Product Plan:

{product_plan}
"""


class CriticAgent:

    def run(self, product_plan):

        prompt = CRITIC_PROMPT.format(
            product_plan=product_plan
        )

        return generate_response(prompt)