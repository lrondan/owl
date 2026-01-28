from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

from .models import QuoteRequest
from .models import Proyecto



def quote(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        company = request.POST.get("company", "").strip()
        service = request.POST.get("service", "").strip()
        message = request.POST.get("message", "").strip()

        # ❌ VALIDACIONES
        if not name:
            messages.error(request, "Name is required.")
        if not email or "@" not in email:
            messages.error(request, "Email is required.")
        elif not phone or not phone.isdigit():
            messages.error(request, "Phone number is required.")
        elif service not in ["Black", "Gray", "White"]:
            messages.error(request, "Please select a valid service.")
        else:
            QuoteRequest.objects.create(
                name=name,
                phone=phone,
                email=email,
                company=company,
                service=service,
                message=message
            )

            send_mail(
                subject="New Quote Request",
                message=f"""
                Name: {name}
                Phone: {phone}
                Service: {service}
                Email: {email}
                Company: {company}

                Message:
                {message}
                """,
                from_email="local@django.com",
                recipient_list=["admin@local.com"],
            )

            messages.success(request, "Your quote request has been sent successfully!")

    return render(request, "quote.html")

def proyectos_destacados(request):
    # Puedes filtrar según GET params si quieres (ej: ?tipo=PENTEST)
    proyectos = Proyecto.objects.filter(destacado=True).order_by('-fecha_publicacion')[:6]
    return render(request, "projects.html", {'proyectos': proyectos})
