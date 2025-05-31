from django.test import TestCase

# Create your tests here.
class HomepageTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class AboutPageTests(TestCase):
    def test_url_exists_At_correct_location(self):
        
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
       