from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from data.models import *
from django.core.mail.backends.smtp import EmailBackend
import requests
import keys

template_1 = """
<html>
<body>
<br>
<h3>Respected Sir/Ma'am</h3><br>
<h5>
<p>We would like it to bring it to your notice that the water constituents of handpump located at %s is currently unsafe for drinking. Kindly visit the link- %s for more information.</p>
<p>Considering the safety of public, we hope that the matter will be resolved soon.</p>
</h5>
</body>
</html>
"""
msg_1="We would like it to bring it to your notice that the water contituents of handpump located at %s is currently unsafe for drinking. Kindly visit the link- %s for more information.Considering the safety of public, we hope that the matter will be resolved soon"

def sendMail(request):
	habitation=request.POST.get('habitation')
	habitation_1=HabitationData.objects.get(name='habitation')
	block1=str(habitation_1.village.panchayat.block)
	#link to be sent in email
	url=''
	temp_html = template_1 % (habitation_1+","+habitation_1.village+","+habitation_1.village.block+","+habitation_1.village.block.district,url)
	msg=msg_1 %(habitation_1+","+habitation_1.village+","+habitation_1.village.block+","+habitation_1.village.block.district,url)
	user=Officials.objects.all()
	email=[]
	for x in user:
		if x.block==block1:		
			mobile=user.mobile
			send_sms(mobile,msg_1,keys.KEY_SENDER_ID)
			email.append(str(user.email))
# heheh
	if len(email)!=0:
		send_mail(
	    'Threat in HandPump',
	    'Here is the message.',
	    'iket.ag24@gmail.com',
	    email,c
	    fail_silently=True,
	    html_message=temp_html,
	    )
		print 'sent'
	
def send_sms(mobile, msg, sender=keys.KEY_SENDER_ID):
    try:
        authkey = keys.KEY_MSG91
        url = 'http://api.msg91.com/api/sendhttp.php?authkey=' + authkey + '&mobiles='
        url += mobile
        url += '&message=' + msg + '%0A'
        url += '&sender=' + sender + '&route=4'
        print url
        print requests.request('GET', url)
    except Exception as e:
        print(str(e))


# Create your views here.
