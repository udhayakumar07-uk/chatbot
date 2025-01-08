import google.generativeai as ai

API_KEY = "AIzaSyBBfzigdlQcIu0ALWmMHCFAw0G_STpYYmo"
ai.configure(api_key=API_KEY)

# Initialize Google AI Chat
def get_chatbot():
    module = ai.GenerativeModel("gemini-pro")
    return module.start_chat()
