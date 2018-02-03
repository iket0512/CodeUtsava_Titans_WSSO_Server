from django.shortcuts import render
from data.models import HabitationElementData, HabitationData, ElementData
# Create your views here.
from datetime import datetime
import pytz
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from decimal import Decimal
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
		tmp['address'] = "%s, %s, %s, %s, %s, %s"%(habitation.name, village.name, panchayat.name, block.name, district.name, state.name)
		tmp['latitude'] = habitation.latitude
		tmp['longitude'] = habitation.longitude
		data.append(tmp)

	return data	

def trigger_post():
	habitation_data = get_habitation_data()
	for habitation in habitation_data():
		if habitation['alert_level'] > 0:
			pass

def pointers(request):
	response = {}
	response['success'] = True
	data = get_habitation_data()
	filtered_data = []
	i = 0
	for points in data:
		if(points['latitude'] != Decimal(0)):
			filtered_data.append(points)
	response['data']=filtered_data

	return JsonResponse(response)

def test(request):
    return render(request,"containers/home.html")

def test_map(request):
    return render(request,"containers/maps.html")
