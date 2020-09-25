from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Course
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login.html'))
    return render(request, 'welcome.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html',{
                'message' : 'Invalid'
            })
    return render(request, 'login.html')


def add_course(request):
    if request.method == 'POST':
        course = Course.objects.filter(cID = request.POST['course_name'])
        student = User.objects.get(pk = request.user.pk)
        if len(course)==1:
            course = course[0]
            if course.status == True:
                if course.enroll.count() < course.quota:
                    course.enroll.add(student)
                    return HttpResponseRedirect(reverse('welcome'))
                else:
                    return render(request, 'addcourses.html', {'error_enroll': 'This course is full'})
            else:
                return render(request, 'addcourses.html', {'error_enroll': 'This course is not open'})
        else:
            return render(request, 'addcourses.html', {'error_enroll': 'Not found this course'})

def cancel_course(request):
    if request.method == 'POST':
        course = Course.objects.filter(cID = request.POST['course_name'])
        student = User.objects.get(pk = request.user.pk)
        if len(course)==1:
            course = course[0]
            course.enroll.remove(student)
            return HttpResponseRedirect(reverse('welcome'))
        else:
            return render(request, 'addcourses.html', {'error_enroll' : 'ไม่ได้ลงทะเบียนวิชานี้'})

def logout_view(request):
    return render(request, 'login.html')


def welcome(request):
    return render(request, 'index.html', {
        'enroll_at' : Course.objects.filter(enroll = request.user.id),
        'not_enroll_at': Course.objects.exclude(enroll = request.user.id)
    })