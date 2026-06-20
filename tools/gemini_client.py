import google.generativeai as genai

from config import GOOGLE_API_KEY, MODEL_NAME

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)


def generate_response(prompt: str):
    try:
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"ERROR: {str(e)}"