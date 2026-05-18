
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Category


class BlogTestBase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="u1",
            password="pass123"
        )
        self.user2 = User.objects.create_user(
            username="u2",
            password="pass123"
        )

        self.post = Post.objects.create(
            title="Test Post",
            body="Body",
            author=self.user1
        )


class TestCRUD(BlogTestBase):

    def test_create_post(self):
        self.client.login(username="u1", password="pass123")
        category = Category.objects.create(name="Social")
        response = self.client.post(
            reverse("blog:create"),
            {
                "title": "New",
                "body": "Testing",
                "categories" : category.id,
                "published_at": "2026-05-14 10:30:00"
            }
        )
        # print(response.context["form"].errors)  # 👈 Add this if has error
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="New").exists())

    def test_read_post(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.get(
            reverse("blog:detail", args=[self.post.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_update_post(self):
        self.client.login(username="u1", password="pass123")
        category = Category.objects.create(name="Social")
        response = self.client.post(
            reverse("blog:edit", args=[self.post.pk]),
            {
                "title": "Updated",
                "body": "Changed",
                "categories" : category.id,
                "published_at": "2026-05-14 10:30:00"
            }
        )
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated")

    def test_delete_post(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.post(
            reverse("blog:delete", args=[self.post.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Post.objects.filter(pk=self.post.pk).exists()
        )


class TestAuthorization(BlogTestBase):

    def test_create_requires_login(self):
        response = self.client.post(
            reverse("blog:create"),
            {"title": "X"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_edit_requires_login(self):
        response = self.client.get(
            reverse("blog:edit", args=[self.post.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_only_author_can_edit(self):
        self.client.login(username="u2", password="pass123")
        response = self.client.get(
            reverse("blog:edit", args=[self.post.pk])
        )
        self.assertNotEqual(response.status_code, 200)

    def test_only_author_can_delete(self):
        self.client.login(username="u2", password="pass123")
        response = self.client.post(
            reverse("blog:delete", args=[self.post.pk])
        )
        self.assertNotEqual(response.status_code, 302)


class TestEdgeCases(BlogTestBase):

    def test_edit_nonexistent_post(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.get(
            reverse("blog:edit", args=[9999])
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_post(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.post(
            reverse("blog:delete", args=[9999])
        )
        self.assertEqual(response.status_code, 404)

    def test_empty_title_validation(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.post(
            reverse("blog:create"),
            {
                "title": "",
                "body": "Body"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required")

    def test_very_long_title(self):
        self.client.login(username="u1", password="pass123")
        response = self.client.post(
            reverse("blog:create"),
            {
                "title": "A" * 1000,
                "body": "Body"
            }
        )
        self.assertEqual(response.status_code, 200)
