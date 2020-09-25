from django.test import TestCase, Client
from .models import Course
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your tests here.


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(
            cID="cn330",
            cName="computer",
            term=1,
            year=2020,
            quota=2,
            status=True
            )
        Course.objects.create(
            cID="cn321",
            cName="network",
            term=1,
            year=2020,
            quota=1,
            status=False
            )




def test_index(self):
    c = Client()
    response = c.get("/projects/")



def test_login_view(self):
    c = Client()
    response = c.post('/login_view/', {'username': 'somsak', 'password': 'mesuk'})
    self.assertEqual(response.status_code, 200)

def test_add_course():
    course = Course.objects.get(cID="cn321")
    student = User.objects.create(first_Name="somsri", last_name="mesuk")
    course.enroll.add(student)
    c= Client()
    response = c.get()
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context)

def test_cancel_course():
    pass

def test_logout_view():
    pass

def test_welcome(self):
    c = Client()
    response = c.get("/projects/")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context["enroll_at"].count(), 2)


