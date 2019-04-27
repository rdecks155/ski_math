from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from . import views

# Create your tests here.

class webpageTests(TestCase):
    def testPlayerHistory(self):
        response = self.client.get(reverse('playerhistory'))
        self.assertEquals(response.status_code, 200)
    
    def testWriteHistory(self):
        response = self.client.get(reverse('writeplayer'))
        self.assertEquals(response.status_code, 200)
    
    def testStats(self):
        response = self.client.get(reverse('stats'))
        self.assertEquals(response.status_code, 200)

    def testTeacherStats(self):
        response = self.client.get(reverse('teacherstats'))
        self.assertEquals(response.status_code, 200)

    def testCertificate(self):
        response = self.client.get(reverse('certificate'))
        self.assertEquals(response.status_code, 200)