from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.mail.backends.smtp import EmailBackend

template_1 = """
<html>
<body>
<br>
<h3>Respected Sir/Ma'am</h3><br>
<h5>
<p>We would like it to bring it to your notice that the water contituents of handpump located at %s is currently unsafe for drinking. Kindly visit the link- %s for more information.</p>
<p>Considering the safety of public, we hope that the matter will be resolved soon.</p>
</h5>
</body>
</html>
"""

def sendMail(request):
	x = template_1 % ('raipur','www.iket.tech')
	send_mail(
    'Test Mail',
    'Here is the message.',
    'iket.ag24@gmail.com',
    ['iket.nit@gmail.com'],
    fail_silently=False,
    html_message=x,
    )
	print 'sent'
	

# Create your views here.
