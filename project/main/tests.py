from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestMainURLs(TestCase):
    def test_home_url_is_correct(self):
        home_url = reverse('main:home')
        self.assertEqual(home_url, '/')

    def test_ask_url_is_correct(self):
        ask_url = reverse('main:ask')
        self.assertEqual(ask_url, '/ask/')


