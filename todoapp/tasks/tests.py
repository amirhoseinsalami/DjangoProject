from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task, Category


class TaskTestBase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="u1",
            password="pass123"
        )
        self.user2 = User.objects.create_user(
            username="u2",
            password="pass123"
        )

        self.task = Task.objects.create(
            title="Test Task",
            description="description",
            user=self.user1
        )


class TestCRUD(TaskTestBase):

    def test_create_task(self):
        self.client.login(username="u1", password="pass123")
        category = Category.objects.create(name="daily life")
        response = self.client.post(
            reverse("tasks:add_task"),
            {
                "title": "New",
                "description": "Testing",
                "categories" : category.id,
                "due_date": "2026-05-14 10:30:00",
                "status" : "IP",
                "priority" : "L"
            }
        )
        # print(response.context["form"].errors)  # 👈 Add this if has error
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title="New").exists())

    def test_read_task(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.get(
            reverse("tasks:task_detail", args=[self.task.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_update_task(self):
        self.client.login(username="u1", password="pass123")
        category = Category.objects.create(name="work")
        response = self.client.post(
            reverse("tasks:edit_task", args=[self.task.pk]),
            {
                "title": "Updated",
                "description": "Changed",
                "categories" : category.id,
                "due_date": "2026-05-14 10:30:00",
                "status" : "P",
                "priority" : "H"
            }
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated")

    def test_delete_task(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.post(
            reverse("tasks:delete_task", args=[self.task.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Task.objects.filter(pk=self.task.pk).exists()
        )


class TestAuthorization(TaskTestBase):

    def test_create_requires_login(self):
        response = self.client.post(
            reverse("tasks:add_task"),
            {"title": "X"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_edit_requires_login(self):
        response = self.client.get(
            reverse("tasks:edit_task", args=[self.task.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_only_author_can_edit(self):
        self.client.login(username="u2", password="pass123")
        response = self.client.get(
            reverse("tasks:edit_task", args=[self.task.pk])
        )
        self.assertNotEqual(response.status_code, 200)

    def test_only_author_can_delete(self):
        self.client.login(username="u2", password="pass123")
        response = self.client.post(
            reverse("tasks:delete_task", args=[self.task.pk])
        )
        self.assertNotEqual(response.status_code, 302)


class TestEdgeCases(TaskTestBase):

    def test_edit_nonexistent_post(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.get(
            reverse("tasks:edit_task", args=[9999])
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_post(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.post(
            reverse("tasks:delete_task", args=[9999])
        )
        self.assertEqual(response.status_code, 404)

    def test_empty_title_validation(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.post(
            reverse("tasks:add_task"),
            {
                "title": "",
                "description": "description"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required")

    def test_very_long_title(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.post(
            reverse("tasks:add_task"),
            {
                "title": "A" * 1000,
                "body": "description"
            }
        )
        self.assertEqual(response.status_code, 200)
