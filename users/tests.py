from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "jakhongir",
                "first_name": "Jakhongir",
                "last_name": "Rakhmonov",
                "email": "jrahmonov2@gmail.com",
                "password": "somepassword"
            }
        )

        user = User.objects.get(username="jakhongir")

        self.assertEqual(user.first_name, "Jakhongir")
        self.assertEqual(user.last_name, "Rakhmonov")
        self.assertEqual(user.email, "jrahmonov2@gmail.com")
        self.assertNotEqual(user.password, "somepassword")
        self.assertTrue(user.check_password("somepassword"))

    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name": "Jakhongir",
                "email": "jrahmonov2@gmail.com"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "jakhongir",
                "first_name": "Jakhongir",
                "last_name": "Rakhmonov",
                "email": "invalid-email",
                "password": "somepassword"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_unique_username(self):
        user = User.objects.create(username="jakhongir", first_name="Jakhongir")
        user.set_password("somepass")
        user.save()

        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "jakhongir",
                "first_name": "Jakhongir",
                "last_name": "Rakhmonov",
                "email": "jrahmonov2@gmail.com",
                "password": "somepassword"
            }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response, "form", "username", "A user with that username already exists.")
