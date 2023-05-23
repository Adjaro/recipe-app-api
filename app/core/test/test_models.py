""""
Tests  for  models
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models



class ModelTest(TestCase):
    """Test models."""

    def test_create_user_whit_email_succes(self):
        """Test creating  a user with  an  email  is  succeful??."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_email_normalized(self):
        """Test  email  is  normalized  for  new  user."""
        sample_email = [
            ["test1@Example.com", "test1@example.com"],
            ["test2@EXAMPLE.com", "test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"]
        ]

        for email, excep in sample_email:
            user = get_user_model().objects.create_user(email, "Sample1234")
            self.assertEqual(user.email, excep)

    def test_user_without_email(self):
        """Test  that  crating  a user  withat an  email  raises  valueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', "Samplepassword1234")

    def test_create_superuser(self):
        """Test  creating a  superuser."""
        user = get_user_model().objects.create_superuser(
            'testadmin@example.com',
            'admin1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test  creating  a  recipe  is  successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )

