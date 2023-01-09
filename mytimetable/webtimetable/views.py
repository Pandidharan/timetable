from django.shortcuts import render

# Create your views here.
def mytimetable(request):
    return render(request,'webtimetable/mytimetable.html')