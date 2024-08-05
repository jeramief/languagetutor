import os
from django.http import JsonResponse
from django.shortcuts import render
from openai import OpenAI

# OPENAI_KEY = os.getenv("OPENAI_KEY")
# openai.api_key = OPENAI_KEY
client = OpenAI(
    # organization="org-fwH02fq9mlwoEZtLUq7rpbel",
    project="proj_YsQfhLjHPSTzEWSIhgQ98fhG",
)


def ask_openai(message):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )

    answer = completion.choice[0].text.strip()
    return answer


def chatbot(request):
    if request.method == "POST":
        message = request.POST.get("message")
        response = ask_openai(message)

        return JsonResponse({"message": message, "response": response})

    return render(request, "chatbot.html")
