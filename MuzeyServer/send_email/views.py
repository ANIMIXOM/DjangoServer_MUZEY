import os
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
from Base.models import Visitor

def send_email(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('email')
        subject = 'Грамота.'
        message = "Поздравляем!!!"
        from_email = 'nikijakushev@yandex.ru'

        email = EmailMultiAlternatives(subject, message, from_email, [recipient_email])

        email.attach_alternative(message, "text/html")

        image_path = 'static/gramota.png'
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype('static/Majestic Regular.ttf', 100)

        first_user = Visitor.objects.last()

        if first_user:
            first_name = first_user.Name
            last_name = first_user.Surname
        else:
            first_name = last_name = None
        text = f"{first_name} {last_name}"
        text_color = (0, 0, 0)
        text_position = (500, 1000)
        draw.text(text_position, text, fill=text_color, font=font)

        output_path = os.path.join(settings.MEDIA_ROOT, 'static/output_image.png')
        image.save(output_path)

        if os.path.exists(output_path):
            print("Изображение успешно создано:", output_path)
            with open(output_path, 'rb') as img:
                email.attach('image1.png', img.read(), 'image/png')
        else:
            print("Ошибка: изображение не создано.")

        email.send()
        os.remove('static/output_image.png')
        return HttpResponse('Письмо с изображением отправлено!')

    return render(request, 'send_email.html')
