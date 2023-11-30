from django.shortcuts import render, redirect
from contact.models import ContactMessage


def send_message(request):
    if request.method == "POST":
        form = ContactMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mensaje_enviado")
    else:
        form = ContactMessage()

    return render(request, "contact/send_message.html", {"form": form})


def sent_message(request):
    return render(request, "contact/sent_message.html")
