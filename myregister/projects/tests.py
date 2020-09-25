from django.test import TestCase, Client
from .models import Course
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
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
        self.user = User.objects.create(username='admin', password='pass@123', email='admin@admin.com')

    def test_index(self):
        c = Client()
        response = c.get("/projects/index/")



    def test_login_view(self):
        c = Client()
        response = c.post('/projects/', {'username': 'somsak', 'password': 'mesuk'})
        c.login()
        response = c.get('/projects/welcome/')
    def test_add_course(self):
        course = Course.objects.get(cID="cn321")
        student = User.objects.create(first_name="somsri", last_name="mesuk")
        course.enroll.add(student)
        c= Client()
        response = c.get("/projects/welcome")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["not_enroll_at"].count(), 1)

    def test_cancel_course(self):
        student = User.objects.create(first_name="somsri", last_name="mesuk")
        course = Course.objects.get(cID="cn321")
        course.enroll.remove(student)
        c= Client()
        response = c.get("/projects/welcome")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["enroll_at"].count(), 2)

    def test_logout_view(self):
        student = User.objects.create(first_name="somsri", last_name="mesuk")
        c = Client()
        c.logout()

    def test_welcome(self):
        c = Client()
        response = c.get("/projects/welcome")
        self.assertEqual(response.status_code, 200)



