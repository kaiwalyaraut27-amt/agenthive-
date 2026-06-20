from tools.validators import (
    detect_prompt_injection,
    detect_api_key
)


class SecurityAgent:

    def run(self, user_input):

        if detect_prompt_injection(user_input):

            return False, "Prompt Injection Detected"

        if detect_api_key(user_input):

            return False, "Possible API Key Detected"

        return True, "Security Check Passed"