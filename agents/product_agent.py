from tools.gemini_client import generate_response
from tools.prompt_templates import (
    PRODUCT_PROMPT,
    IMPROVEMENT_PROMPT
)


class ProductAgent:

    def run(
        self,
        research,
        competitors,
        personas
    ):

        prompt = PRODUCT_PROMPT.format(
            research=research,
            competitors=competitors,
            personas=personas
        )

        return generate_response(prompt)

    def improve_plan(
        self,
        product_plan,
        feedback
    ):
        prompt = IMPROVEMENT_PROMPT.format(
            product_plan=product_plan,
            feedback=feedback
        )

        return generate_response(prompt)