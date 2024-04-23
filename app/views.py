from django.shortcuts import render

# Create your views here.
from app.models import Student

def Student_data(request):
    Student_list=Student.objects.all()
    my_dict={'Student_list':Student_list}
    return render(request,'index.html',my_dict)
