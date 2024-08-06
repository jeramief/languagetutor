import os
from django.http import JsonResponse
from django.shortcuts import render
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# OPENAI_KEY = os.getenv("OPENAI_KEY")
# openai.api_key = OPENAI_KEY
client = OpenAI(
    # organization=os.getenv("OPENAI_ORGANIZATION_KEY"),
    project=os.getenv("OPENAI_PROJECT_KEY"),
)


def ask_openai(message):
    completion = client.chat.completions.create(
        model="gpt-3-5",
        messages=[
            {"role": "user", "content": "You are a native Japanese speaker"},
            {"role": "user", "content": message},
        ],
    )

    answer = completion.choice[0].text.strip()
    return answer


def chatbot(request):
    if request.method == "POST":
        message = request.POST.get("message")
        response = ask_openai(message)

        return JsonResponse({"message": message, "response": response})

    return render(request, "chatbot.html")
