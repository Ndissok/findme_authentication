from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import SESSION_KEY

# Create your tests here.

class LoginViewTests(TestCase):
    """
    Tests for the authentication (login) page.
    - Rendering of the login page
    - Valid login
    - Invalid login
    - Redirection for already authenticated users
    """
    def setUp(self):
        self.user_model = get_user_model()
        self.password = "testpassword123"
        self.user = self.user_model.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password=self.password
        )
        self.login_url = reverse("login")
        self.dashboard_url = reverse("dashboard")

    def test_login_page_renders(self):
        """The login page should render for anonymous users."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nom d&#x27;utilisateur")

    def test_valid_login(self):
        """A user can log in with valid credentials and is redirected to dashboard."""
        response = self.client.post(self.login_url, {
            "username": self.user.username,
            "password": self.password
        }, follow=True)
        self.assertRedirects(response, self.dashboard_url)
        self.assertIn(SESSION_KEY, self.client.session)

    def test_invalid_login(self):
        """Invalid credentials should not log the user in and should show the form again."""
        response = self.client.post(self.login_url, {
            "username": self.user.username,
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nom d&#x27;utilisateur")
        self.assertNotIn(SESSION_KEY, self.client.session)

    def test_authenticated_user_redirected(self):
        """An already authenticated user should be redirected to dashboard."""
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(self.login_url)
        self.assertRedirects(response, self.dashboard_url)
