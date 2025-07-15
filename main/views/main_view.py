from django.shortcuts import render, redirect
from main.models.main_model import FAQ, Contact, CustomerOpinion, Portfolio
import re
import requests

def home(request):
    if request.method == 'POST':
        name = request.POST.get('first-name')
        phone = request.POST.get('phone')

        bot_token = "7580116305:AAHV8MCjJDLWxPiFq9jrUmr8yJKZJm0ekUU"
        chat_id = "-1002888958348"

        # 1. Foydalanuvchi ma’lumotlari to‘ldirilganmi?
        if not all([name, phone]):
            return render(request, 'index.html', {'error': 'Ism va telefon raqami to‘ldirilishi shart!'})

        # 2. Telefon raqamdagi bo‘sh joylarni olib tashlash
        phone = phone.replace(' ', '')  # Masalan: +998945454541

        # 3. Raqam to‘g‘ri formatda kiritilganmi? (faqat +998XXXXXXXXX)
        if not re.match(r'^\+998\d{9}$', phone):
            return render(request, 'index.html', {'error': 'Telefon raqami noto‘g‘ri formatda! (+998 XX XXX XX XX)'})

        # 4. Bazaga yozish
        try:
            Contact.objects.create(name=name, phone=phone)
        except Exception as e:
            print("❌ Bazaga yozishda xatolik:", e)
            return render(request, 'index.html', {'error': 'Saqlashda xatolik yuz berdi.'})

        # 5. Telegramga xabar yuborish
        message = (
            f"🆕 Yangi Lead qo'shildi:\n"
            f"👤 Ismi: {name}\n"
            f"📞 Telefon raqami: {phone}"
        )
        send_telegram_message(bot_token, chat_id, message)

        # 6. Muvaffaqiyatli redirect
        return redirect('main:home')

    # Agar GET bo‘lsa — sahifadagi ma’lumotlar
    contact = Contact.objects.all()
    customer_opinion = CustomerOpinion.objects.all()
    portfolio = Portfolio.objects.all()
    faq = FAQ.objects.all()

    context = {
        'contact': contact,
        'opinions': customer_opinion,
        'portfolios': portfolio,
        'faqs': faq
    }
    return render(request, 'index.html', context)

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("❌ Telegramga yuborishda xatolik:", e)
