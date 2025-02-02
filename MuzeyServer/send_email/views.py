import os
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont


def send_email(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('email')
        subject = 'Грамота.'
        message = "Поздравляем!!!"
        from_email = 'nikijakushev@yandex.ru'
        name = request.POST.get('name')
        surname = request.POST.get('surname')

        email = EmailMultiAlternatives(subject, message, from_email, [recipient_email])
        email.attach_alternative(message, "text/html")

        image_path = 'static/gramota.png'
        output_path = os.path.join(settings.MEDIA_ROOT, 'output_image.png')

        try:
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('static/Majestic Regular.ttf', 100)
        except Exception as e:
            return HttpResponse(f"Ошибка при работе с изображением: {e}", status=500)

        text = f"{name} {surname}"
        text_color = (0, 0, 0)
        text_position = (500, 1000)

        try:
            draw.text(text_position, text, fill=text_color, font=font)
        except Exception as e:
            return HttpResponse(f"Ошибка при добавлении текста к изображению: {e}", status=500)

        try:
            image.save(output_path)
            with open(output_path, 'rb') as img:
                email.attach('image1.png', img.read(), 'image/png')
        except Exception as e:
            return HttpResponse(f"Ошибка при сохранении и прикреплении изображения: {e}", status=500)

        try:
            email.send()
        except Exception as e:
            return HttpResponse(f"Ошибка при отправке письма: {e}", status=500)
        finally:
            try:
                os.remove(output_path)
            except FileNotFoundError:
                pass

        return redirect('/')
    return render(request, 'send_email.html')
