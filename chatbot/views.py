from django.http import JsonResponse
from django.shortcuts import render


def chatbot(request):
    if request.method == "POST":
        message = request.POST.get("message")
        response = "Howdy"

        print("in if")

        return JsonResponse({"message": message, "response": response})

    print("out if")

    return render(request, "chatbot.html")
