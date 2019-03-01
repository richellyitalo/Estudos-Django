from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.error(request, 'Você já realizou uma solicitação para esse imóvel')
                return redirect('/listings/' + listing_id)

        contact = Contact(
            listing=listing, listing_id=listing_id, name=name, email=email,
            phone=phone, message=message, user_id=user_id
        )

        contact.save()

        # send_mail(
        #     'Nova solicitação',
        #     'Você recebeu uma nova solicitação de imóvel.<br/>Acesse o painel administrativo.',
        #     'admin@django.com',
        #     [realtor_email],
        #     fail_silently=False,
        #     html_message='Você recebeu uma nova solicitação de imóvel.<br/>Acesse o painel administrativo.'
        # )

        messages.success(request, 'Recebemos sua solicitação. Em breve entraremos em contato')

        return redirect('/listings/' + listing_id)
