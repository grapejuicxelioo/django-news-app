from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class UserManagerTests(TestCase):
  def test_create_user(self):
    User = get_user_model()
    user = User.objects.create_user(
      username="testuser",
      email="testuser@ejemplo.com",
      password="testpass1234",
    )

    self.assertEqual(user.username, "testuser")
    self.assertEqual(user.email, "testuser@ejemplo.com")
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)

  def test_create_superuser(self):
    User = get_user_model()
    admin_user = User.objects.create_superuser(
      username="testsuperuser",
      email="testsuperuser@ejemplo.com",
      password="testpass1234"
    )

    self.assertEqual(admin_user.username, "testsuperuser")
    self.assertEqual(admin_user.email, "testsuperuser@ejemplo.com")
    self.assertTrue(admin_user.is_active)
    self.assertTrue(admin_user.is_staff)
    self.assertTrue(admin_user.is_superuser)
