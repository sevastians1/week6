from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student
# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

@csrf_exempt
def add_student(request):
    if request.method=='POST':
        print('recieved')
        body=json.loads(request.body)
        print(body)
        print(body['first_name'], body['last_name'], body['email'])
        new_student=Student(first_name=body['first_name'], last_name=body['last_name'], email=body['email'])
        new_student.save()
#    print(request.method)
    return JsonResponse({'status':200})

def side_page(request):

    print(Student.objects.all())
    return JsonResponse({'status':200})