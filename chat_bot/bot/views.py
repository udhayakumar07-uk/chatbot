from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .google_ai import get_chatbot
from .forms import CustomLoginForm, CustomSignupForm

# Start chat session
chat = get_chatbot()
def chatbot(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        if user_message.lower() == "bye":
            return JsonResponse({"response": "Goodbye!"})
        response = chat.send_message(user_message)
        return JsonResponse({"response": response.text})
    return render(request, "chatbot.html")

def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        response_text = f"You said: {user_message}"  # Replace this with your chatbot logic
        return JsonResponse({"response": response_text})
def auth_view(request):
    login_form = CustomLoginForm(data=request.POST or None)
    signup_form = CustomSignupForm(request.POST or None)

    if request.method == "POST":
        if "username_or_email" in request.POST:
            if login_form.is_valid():
                username_or_email = login_form.cleaned_data["username_or_email"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username_or_email, password=password)
                if user:
                    login(request, user)
                    return redirect("chatbot")
                else:
                    return JsonResponse({"success": False, "error": "Invalid username or password."})
        elif "username" in request.POST:
            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.set_password(signup_form.cleaned_data["password"])
                user.save()
                login(request, user)
                return redirect("chatbot")

    return render(request, "login.html", {"login_form": login_form, "signup_form": signup_form})
