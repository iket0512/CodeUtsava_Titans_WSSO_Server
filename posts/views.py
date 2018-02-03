from django.shortcuts import render
from data.models import HabitationElementData, HabitationData, ElementData, Officials
# Create your views here.
from datetime import datetime
import pytz, uuid
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from decimal import Decimal
from .models import PostsData

def today():
	return make_aware(datetime.now())

def make_aware(time):
	timezone = pytz.timezone('Asia/Kolkata')
	return timezone.localize(time)

def get_habitation_data():
	data = []
	today_date = today().date()
	for habitation in HabitationData.objects.all():
		tmp = {}
		tmp['elements'] = []
		tmp['alert_level'] = 0
		for element in ElementData.objects.all():
			tmp_tmp = {}
			print "thisthis", today_date
			print habitation.name, habitation.village.name, habitation.village.panchayat.name, habitation.village.panchayat.block.name, habitation.village.panchayat.block.district.name
			print element
			habitationElement = HabitationElementData.objects.get(created__date = today_date,
				habitation = habitation,
				element = element)
			tmp_tmp['name'] = element.name
			tmp_tmp['count'] = habitationElement.count
			tmp_tmp['limit'] = element.permissible_limit_high
			alert_level = 0
			if(habitationElement.count >= element.permissible_limit_low):
				alert_level = 1
			if(habitationElement.count >= element.permissible_limit_high):
				alert_level = 2

			if alert_level > tmp['alert_level']:
				tmp['alert_level'] = alert_level

			tmp_tmp['alert_level'] = alert_level
			# tmp_tmp['hazards'] = element.hazards
			# tmp_tmp['remedy'] = element.remedy
			tmp['elements'].append(tmp_tmp)

		village = habitation.village
		panchayat = village.panchayat
		block = panchayat.block
		district = block.district
		state = district.state
		tmp['hid'] = habitation.id
		tmp['address'] = "%s, %s, %s, %s, %s, %s"%(habitation.name, village.name, panchayat.name, block.name, district.name, state.name)
		tmp['latitude'] = habitation.latitude
		tmp['longitude'] = habitation.longitude
		data.append(tmp)

	return data	

template_1 = """<html><body><br><h3>Respected Sir/Ma'am</h3><br><h5><p>
We would like it to bring it to your notice that the water constituents of handpump located at %s is currently unsafe for drinking. Kindly visit the link- %s for more information.</p>
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

	content_email = template_1%(habitation_json['address'], post.id, details)
	# sendmail(emails, content_email)
	# sendsms(mobiles, content_sms)

def get_posts(request):
	response = {}
	response['data'] = []
	for posts in PostsData.objects.all():
		tmp = {}
		tmp['id'] = posts.uid
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

	return JsonResponse(response)

def test(request):
    return render(request,"containers/home.html")

def test_map(request):
    return render(request,"containers/maps.html")
