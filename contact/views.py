from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def contact_page(request):
    message_sent = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"From: {name}\nEmail: {email}\n\n{message}"

        # send email
        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            ['himalayaroadsafety@gmail.com'],  # your inbox
        )

        message_sent = True

    return render(request, "contact/contact.html", {
        "message_sent": message_sent
    })
