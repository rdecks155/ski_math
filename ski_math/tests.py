from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from . import views
import json

# Create your tests here.

class webpageTests(TestCase):
    def testPlayerHistory(self):
        response = self.client.get(reverse('playerhistory'))
        self.assertEquals(response.status_code, 200)
        # self.assertEqual(json.loads(response.content)['data'],[])
        #test response is json
    
    def testWriteHistory(self):
        response = self.client.get(reverse('writeplayer'))
        self.assertEquals(response.status_code, 200)
        #test that the database is changed 
    
    def testStats(self):
        response = self.client.get(reverse('stats'))
        self.assertEquals(response.status_code, 200)

    def testTeacherStats(self):
        response = self.client.get(reverse('teacherstats'))
        self.assertEquals(response.status_code, 200)

    def testCertificate(self):
        response = self.client.get(reverse('certificate'))
        self.assertEquals(response.status_code, 200)