from django.shortcuts import render, redirect
from .models import Contact, Email
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

#Create database view and model:

def inquiry(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        car_id = request.POST['car_id']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car')
                return redirect('/cars/'+car_id)

        contact = Contact(first_name=first_name, last_name=last_name, car_id=car_id, 
        customer_need=customer_need, car_title=car_title, city=city, state=state, 
        email=email, phone=phone, message=message, user_id=user_id)



#Sending notification mails:
        #admin_info = User.objects.get(is_superuser=True)
        #admin_email = admin_info.email

        #send_mail(
        #    'New Car Inquiry',
        #    'You have new inquiry for' + car_title + ' car. Please login into your account for more info',
        #    'asgarov.emin@gmail.com',
        #    ['emin_a7@hotmail.com'],
        #    fail_silently=False,
        #)

#Saving in DB:

        contact.save()

        messages.success(request, 'Your request has been submitted')
        return redirect('/cars/'+car_id)


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        subject = request.POST['subject']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        

        email_contact = Email(first_name=first_name, subject=subject, email=email, phone=phone, message=message)

        email_contact.save()
    
        messages.success(request, 'Your request has been submitted')

    return render(request, 'pages/contact.html')