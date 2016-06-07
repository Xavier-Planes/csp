from django.test import TestCase
from models import *
from django.utils import timezone
from django.core.urlresolvers import reverse
from forms import *
import unittest


class CreationTest(TestCase):

    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def create_project(self, name="test_name", description="description test", link="https://www.google.es/"):
        return Project.objects.create(name=name, description=description, link=link)

    def create_department(self, name="test_name"):
        return Department.objects.create(name=name)

    def create_review(self, comment="test_comment"):
        return Review.objects.create(comment=comment)

    def create_activity(self, title="test_title", description="test_description", statement="test_statement"):
        return Activity.objects.create(title=title, description=description, statement=statement)

    def create_answer(self, body="test_body"):
        return Answer.objects.create(body=body)

    def test_project_creation(self):
        instance_under_test = self.create_project()
        self.assertTrue(isinstance(instance_under_test, Project))
        self.assertEqual(instance_under_test.__unicode__(), str(instance_under_test.id))

    def test_department_creation(self):
        instance_under_test = self.create_department()
        self.assertTrue(isinstance(instance_under_test, Department))
        self.assertEqual(instance_under_test.__unicode__(), str(instance_under_test.id))

    def test_review_creation(self):
        instance_under_test = self.create_review()
        self.assertTrue(isinstance(instance_under_test, Review))
        self.assertEqual(instance_under_test.__unicode__(), str(instance_under_test.id))

    def test_activity_creation(self):
        instance_under_test = self.create_activity()
        self.assertTrue(isinstance(instance_under_test, Activity))
        self.assertEqual(instance_under_test.__unicode__(), str(instance_under_test.id))

    def test_answer_creation(self):
        instance_under_test = self.create_answer()
        self.assertTrue(isinstance(instance_under_test, Answer))
        self.assertEqual(instance_under_test.__unicode__(), str(instance_under_test.id))
