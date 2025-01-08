import google.generativeai as ai

API_KEY = "your_api_key"
ai.configure(api_key=API_KEY)

# Initialize Google AI Chat
def get_chatbot():
    module = ai.GenerativeModel("gemini-pro")
    return module.start_chat()
