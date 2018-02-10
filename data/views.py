from django.shortcuts import render
from models import *
from django.http import JsonResponse
from test_data import load_data, element_data
# Create your views here.
from decimal import Decimal
import requests, json, multiprocessing as mp
from datetime import datetime
import pytz
from django.utils.dateparse import parse_datetime
import time

from django import db

SUCCESS = {
	"success":True
}


def api_call(url, habitation):

	response = requests.get(url)
	# print response.status_code
	data = json.loads(response.text)
	if data['status'] != 'ZERO_RESULTS':
		print data
		location =  data['results'][0]['geometry']['location']
		latitude = location['lat']
		longitude = location['lng']
		print latitude, longitude
		habitation.latitude = latitude
		habitation.longitude = longitude
		habitation.save()
		# print habitation, village

def get_location(habitation):
	# key = 'AIzaSyBiDPRoTGjbRV5j32_Gay-DpmecHMHOtlQ'
	key = 'AIzaSyCSwSH0CtyyFGbnJ3id89GfKVYn9tNbPl4'
	village = habitation.village
	panchayat = village.panchayat
	block = panchayat.block
	district = block.district

	# address = "%s+%s+%s+%s+%s"%(habitation.name, village.name, panchayat.name, block.name, district.name)
	address = "%s+%s"%(panchayat.name, district.name)

	url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'
	url = url%(address, key)
	p = mp.Process(target = api_call, args = (url, habitation))
	time.sleep(.1)
	db.connections.close_all()
	p.start()

def today():
	return make_aware(datetime.now()).date()

def make_aware(time):
	timezone = pytz.timezone('Asia/Kolkata')
	return timezone.localize(time)

def load(data_list):
	keys = ['state', 'district', 'block', 'panchayat', 'village', 'habitation', 'element', 'count']
	statment = "%s='%s'"
	for data in data_list:
		for key in keys:
			exec(statment%(key, data[key]))

		count = Decimal(count)
		# print data,count
		# for key in keys:
		# 	print key, eval(key)

		state, state_created = StateData.objects.get_or_create(name = state)
		district, district_created = DistrictData.objects.get_or_create(state = state, name = district)
		block, block_created = BlockData.objects.get_or_create(district = district, district__state = state, name = block)
		panchayat, panchayat_created = PanchayatData.objects.get_or_create(block = block, block__district = district, block__district__state = state, name = panchayat)
		village, village_created = VillageData.objects.get_or_create(panchayat = panchayat, panchayat__block = block, panchayat__block__district = district, panchayat__block__district__state = state, name = village)
		habitation, habitation_created = HabitationData.objects.get_or_create(village = village, village__panchayat__block = block, village__panchayat__block__district = district, village__panchayat__block__district__state = state, name = habitation)
		# if habitation_created :
		# 	get_location(habitation)
		# 	pass
		
		
		if habitation_created:
			for element_this in ElementData.objects.all():
				H,c = HabitationElementData.objects.get_or_create(habitation = habitation, element = element_this, created= today())
			# print H,c
		print "xxxxxxxxxxxxxxxxx",element
		element = ElementData.objects.get(name = element)
		HE = HabitationElementData.objects.get(habitation = habitation, element = element, created = today())
		# print count
		HE.count = count
		HE.save()
	#check and notify


def populate(request):
	# if(ElementData.objects.all().count() == 0):
	# 	for element in element_data:
	# 		print "\n\n\n..",element['permissible_limit_high'],"\n\n\n\n."
	# 		ElementData.objects.get_or_create(name = element['name'],
	# 			hazards = element['hazards'],
	# 			remedy = element['remedy'],
	# 			permissible_limit_low = element['permissible_limit_low'],
	# 			permissible_limit_high = element['permissible_limit_high'])
	# load(load_data())

	for habitation in HabitationData.objects.filter(latitude = Decimal(0)):
		get_location(habitation)

	return JsonResponse(SUCCESS)
