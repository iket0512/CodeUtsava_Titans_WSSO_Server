from django.shortcuts import render

import csv
from django import forms


# Create your views here.


@csrf_exempt
def export_codenesia_csv(request):
	response_json={}
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="codenesia_data.csv"'

	writer = csv.writer(response)
	writer.writerow(["id", "name","mobile","email","college","userid","score"])

	users = CodenesiaData.objects.all().values_list("id", "name","mobile","email","college","userid","score")
	for user in users:
		writer.writerow(user)

	return response

class UploadFileForm(forms.Form):
	file = forms.FileField()

@csrf_exempt
def import_login_table(request):
	if request.user.is_authenticated():
		user=str(request.user)
		try:
			if request.method == "POST":
				form = UploadFileForm(request.POST,request.FILES)
				if form.is_valid():
					request.FILES['file'].save_to_database(model=ReceiverData,mapdict=['id','name','mobile','email','branch','batch_year'])
					return HttpResponse("OK")
				else:
					return HttpResponseBadRequest()
			else:
				form = UploadFileForm()
				return render(request,'upload.html',{'form':form ,'msg':"Upload table"})
		except Exception as e:
			print str(e);
			return HttpResponse("Page not found")

	return HttpResponse("<H1>404 PAGE NOT FOUND</H1>")