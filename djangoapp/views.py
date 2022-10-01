from django.shortcuts import render
from django.contrib.auth import authenticate
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client
from djangoapp.models import LoginUser

def indexView(request):
    resp_msg={'insert_content':'Welcome to the homepage'}
    return render(request,'index.html',context=resp_msg)

def loginView(request):
    return render(request,'login.html')   


def authView(request):
    uname=request.POST.get('uname')
    upass=request.POST.get('upass')
    userdata = LoginUser.objects.values_list('uname','pword')
    
    for record in userdata:
        print(record[0])
        if record[0]!=uname:
            continue
        else:
            if record[1]==upass:
                resp_msg={'insert_content':'Login successful'}
                return render(request,'index.html',context=resp_msg)
            else:
                resp_msg={'insert_content':'Invalid password'}
                return render(request,'index.html',context=resp_msg)
            
    resp_msg={'insert_content':'Invalid user'}
    return render(request,'index.html',context=resp_msg) 


def broadcast_sms(request):
    message_to_broadcast = ("Meassage from Deepika broadcast as Hello Twilio")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)       


        

