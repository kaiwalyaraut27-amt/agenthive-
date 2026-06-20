def detect_prompt_injection(text):

    suspicious_words = [

        "ignore all instructions",

        "forget previous instructions",

        "system prompt",

        "developer instructions",

        "override security"
    ]

    text = text.lower()

    for word in suspicious_words:

        if word in text:

            return True

    return False


def detect_api_key(text):

    suspicious_patterns = [

        "sk-",

        "AIza",

        "api_key",

        "access_token"
    ]

    for pattern in suspicious_patterns:

        if pattern in text:

            return True

    return False