from django.test import TestCase
import time
from django.test import Client
from django.urls import reverse
from appflow.models import Project
# Create your tests here.

class TaskTestcase(TestCase):
    def setUp(self):
        Project.objects.create(
            project="Test_Project_Case"
        )
        time.sleep(1)
        Project.objects.create(
            project="Test_Project_Case_2"
        )
        self.client = Client()

    def test_project_retrieval(self):
        proj = Project.objects.get(project="Test_Project_Case")
        print(proj.created_on)
        self.assertEqual("Test_Project_Case", proj.project)


    def test_project_count(self):
        proj = Project.objects.all()
        self.assertEqual(2, proj.count())

    def test_project_order(self):
        proj = Project.objects.all().order_by('-created_on')
        print(proj)
        self.assertEqual(proj[0].project, "Test_Project_Case_2")

    def test_view_home(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_view_today_task(self):
        response = self.client.get(reverse('project_Specific', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 200)
