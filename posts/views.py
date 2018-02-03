from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt


# Create your views here.



@csrf_exempt
def test(request):
    return render(request,"containers/home.html")

@csrf_exempt
def test_map(request):
    return render(request,"containers/maps.html")

@csrf_exempt
def test_post_comment(request):
    return render(request,"containers/post_insight.html")
