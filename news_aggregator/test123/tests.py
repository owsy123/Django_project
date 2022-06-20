from django.test import TestCase
from django.urls import reverse,resolve
from test123.models import Favourite
from .views import index
from django.test import RequestFactory, TestCase

from test123.views import favourite, index

class TestModel(TestCase):

    def test_news_page_load(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8000/news')
        self.assertEqual(response.status_code, 200)

    def test_news_with_search(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8000/news?query=cricket')
        self.assertEqual(response.status_code, 200)     

    def test_favourite_page_load(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8000/news/favourite?user=owais')
        self.assertEqual(response.status_code, 200)

    def test_favourite_with_id_post(self):
        """The index page loads properly"""
        response = self.client.post('http://localhost:8000/news/favourite?user=owais&id=114')
        self.assertEqual(response.status_code, 200)
