from django.core.mail import send_mail
from django.http import HttpResponse

from book_u5.settings import EMAIL_HOST_USER as email

def send_email_u5(request):
    send_mail(
        subject="Bugun havo qanday",
        message="Havo qanday ko'chaga qarachi",
        from_email="aliyer.temur95@gmail.com",
        recipient_list=[email,"yodgorqoziyev3@gmail.com"],
        fail_silently=False,

    )
    return HttpResponse("success")




from django.core.mail import EmailMultiAlternatives


def send_html_email():
    subject = "HTML email sinovi"

    from_email = "aliyer.temur95@gmail.com"

    to = [ "aliyer.temur95@gmail.com","ulugbeksodiqov599@gmail.com"]

    text_content = "Bu oddiy email matni."

    html_content = f"<h1>Salom</h1><p>Bu <strong>HTML</strong> email. < / p >  <h3>{text_content}</h3></p>"

    email = EmailMultiAlternatives(subject, text_content,
                                   from_email, to)

    email.attach_alternative(html_content, "text/html")

    email.send()
    return HttpResponse("success")
