from django.shortcuts import render
from data.models import HabitationElementData, HabitationData, ElementData, Officials
# Create your views here.
from datetime import datetime
import pytz, uuid, requests
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from decimal import Decimal
from .models import PostsData, ExtendedHabitationElementsData
from django.core.mail import send_mail

from plotly.offline import plot
from plotly.graph_objs import Bar, Scatter, Figure, Layout
from datetime import datetime

sent = False
esent = False

def today():
	return make_aware(datetime.now()).date()

def make_aware(time):
	timezone = pytz.timezone('Asia/Kolkata')
	return timezone.localize(time)

def get_habitation_data():
	print datetime.now()
	data = []

	for ehed in ExtendedHabitationElementsData.objects.filter(created = today()).exclude(habitation__latitude = Decimal(0)):
		tmp = {}

		habitation = ehed.habitation
		# village = habitation.village
		# panchayat = village.panchayat
		# block = panchayat.block
		# district = block.district
		# state = district.state

		hid = habitation.id
		tmp['hid'] = hid
		tmp['latitude'] = ehed.latitude
		tmp['longitude'] = ehed.longitude
		tmp['alert_level'] = ehed.alert_level

		tmp['address'] = habitation.address#"%s, %s, %s, %s, %s, %s"%(habitation.name, village.name, panchayat.name, block.name, district.name, state.name)

		tmp['elements'] = []
		
		element_f = {}
		element_f['name'] = 'Fluoride'
		element_f['limit'] = ehed.f_l
		element_f['count'] = ehed.f_count
		element_f['alert_level'] = ehed.f_al	
		tmp['elements'].append(element_f)

		element_fe = {}
		element_fe['name'] = 'Iron'
		element_fe['limit'] = ehed.fe_l
		element_fe['count'] = ehed.fe_count
		element_fe['alert_level'] = ehed.fe_al	
		tmp['elements'].append(element_fe)

		element_as = {}
		element_as['name'] = 'Arsenic'
		element_as['limit'] = ehed.as_l
		element_as['count'] = ehed.as_count
		element_as['alert_level'] = ehed.as_al	
		tmp['elements'].append(element_as)

		element_n = {}
		element_n['name'] = 'Nitrate'
		element_n['limit'] = ehed.n_l
		element_n['count'] = ehed.n_count
		element_n['alert_level'] = ehed.n_al	
		tmp['elements'].append(element_n)

		element_s = {}
		element_s['name'] = 'Salinity'
		element_s['limit'] = ehed.s_l
		element_s['count'] = ehed.s_count
		element_s['alert_level'] = ehed.s_al	
		tmp['elements'].append(element_s)

		data.append(tmp)

	print datetime.now()
	print data[:1]
	return data

template_1 = """<html><body><br><h3>Respected Sir/Ma'am</h3><br><h5><p>
We would like it to bring it to your notice that the water constituents of handpump located at %s is currently unsafe for drinking. Kindly visit the <a href="%s">link</a> for more information.</p>
<p>Considering the safety of public, we hope that the matter will be resolved soon.</p>
<p>Details:<br>
<ol>
%s
</ol>
</p>
</h5></body></html>"""

element_detail = """
	<li>Name:%s</li>
	<ul>
	<li>Hazards:%s</li>
	<li>Remedies:%s</li>
	</ul>
"""

sms = """Alert HandPump : %s
Kindly look into the matter as soon as possible
%s"""

def notify(post, habitation_json):
	habitation = post.habitation
	village = habitation.village
	panchayat = village.panchayat
	block = panchayat.block
	emails = []
	mobiles = []
	for official in Officials.objects.filter(block = block):
		emails.append(official.email)
		mobiles.append(official.mobile)

	details = ''

	for element in post.data['elements']:
		if element['alert_level'] > 0:
			element_obj = ElementData.objects.get(name = element['name'])
			details = details + element_detail%(element['name'], element_obj.hazards, element_obj.remedy)

	link = "http://172.16.20.190:8000/post/" + str(post.id)
	content_email = template_1%(habitation_json['address'], link, details)

	if len(emails) > 0:
		emails = emails[0]
		print emails
		global esent
		if esent == False:
			send_mail('HandPump Alert!!','Here is the message.','iket.ag24@gmail.com',[emails],fail_silently=True,html_message=content_email)
			esent = True
			print "sent"

	for mobile in mobiles:
		print mobile
		authkey = '120246AD8NbKHar5912cd2b'
		url_sms = 'http://api.msg91.com/api/sendhttp.php?authkey=' + authkey + '&mobiles='
		print url_sms
		url_sms = url_sms + str(mobile)
		url_sms = url_sms + '&message=' + sms%(habitation.name, link) + '%0A'
		url_sms = url_sms + '&sender=' + 'MYWSSO' + '&route=4'
		print url_sms
		global sent
		if(sent == False):
			print requests.request('GET', url_sms)
			sent = True


	# sendmail(emails, content_email)
	# sendsms(mobiles, content_sms)



def get_posts(request):
	response = {}
	response['data'] = []
	for posts in PostsData.objects.all():
		tmp = {}
		tmp['id'] = posts.id
		tmp['data'] = posts.data
		response['data'].append(tmp)

	print "zzxx", response
	return render(request, 'containers/home.html', response)

def trigger_post(request):
	habitation_data = get_habitation_data()
	for post in PostsData.objects.all():
		post.status = 0
		post.save()

	for habitation in habitation_data:
		if habitation['alert_level'] > 0:
			habitation_obj = HabitationData.objects.get(id = habitation['hid'])
			post = PostsData.objects.create(uid = str(uuid.uuid4()),
				status = habitation['alert_level'],
				data = habitation,
				habitation = habitation_obj)
		notify(post, habitation)



def pointers(request):
	response = {}
	response['success'] = True
	data = get_habitation_data()
	filtered_data = []
	i = 0
	for points in data:
		if(points['latitude'] != Decimal(0)):
			filtered_data.append(points)
	response['data'] = filtered_data

	return filtered_data
	# return JsonResponse(response)

def test(request):
    return render(request,"containers/home.html")

def test_map(request):
	data=pointers(request)
	context = {
	"data" : data
	}
	return render(request,"containers/maps.html",context)

def get_post_id(request, id):
	post = PostsData.objects.get(id = int(id))
	response = {}
	response['uid'] = post.uid
	response['status'] = post.status
	response['data'] = post.data

	for element in response['data']['elements']:
		element_obj = ElementData.objects.get(name = element['name'])
		element['hazards'] = element_obj.hazards
		element['remedies'] = element_obj.remedy

	return render(request, "containers/post_insight.html", response)

def get_habitation(request, id):
	response = {}
	habitation = HabitationData.objects.get(id = int(id))
	village = habitation.village
	panchayat = village.panchayat
	block = panchayat.block
	response['address'] = "%s, %s, %s, %s, %s, %s"%(habitation.name, village.name, panchayat.name, block.name, block.district.name, block.district.state.name)
	response['latitude'] = habitation.latitude
	response['longitude'] = habitation.longitude
	# response['graph']={
	Fex=[]
	Fey=[]
	Asx=[]
	Asy=[]
	Fx=[]
	Fy=[]
	Sx=[]
	Sy=[]
	Nx=[]
	Ny=[]
	# }
	for hed in HabitationElementData.objects.filter(habitation = habitation):
		if hed.element.name == "Iron":
			Fex.append(hed.created)
			Fey.append(float(hed.count))
		if hed.element.name == "Arsenic":
			Asx.append(hed.created)
			Asy.append(float(hed.count))
		if hed.element.name == "Fluoride":
			Fx.append(hed.created)
			Fy.append(float(hed.count))
		if hed.element.name == "Nitrate":
			Nx.append(hed.created)
			Ny.append(float(hed.count))
		if hed.element.name == "Salinity":
			Sx.append(hed.created)
			Sy.append(float(hed.count))

	response['Feg'] = plot([Scatter(x=Fex, y=Fey)],auto_open=False,output_type='div')
	response['Asg'] = plot([Scatter(x=Asx, y=Asy)],auto_open=False,output_type='div')
	response['Fg'] = plot([Scatter(x=Fx, y=Fy)],auto_open=False,output_type='div')
	response['Sg'] = plot([Scatter(x=Sx, y=Sy)],auto_open=False,output_type='div')
	response['Ng'] = plot([Scatter(x=Nx, y=Ny)],auto_open=False,output_type='div')

	# print response

	context ={
		"data" :response
	}
	return render(request,"containers/graphs.html",context)

def get_mobileposts(request):
	response = {}
	response['value'] = []
	for posts in PostsData.objects.all():
		response['value'].append(posts.data)

	print "zzxx", response
	return JsonResponse(response)