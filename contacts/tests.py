from django.test import TestCase
from . models import Contact


class ModelTesting(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(full_name='michael', relationship='brother',
         email='michael1234@gmail.com',phone_number="+234817779056",address="lagos,Nigeria")

    def test_contact_model(self):
        d = self.contact
        self.assertTrue(isinstance(d, Contact))
        self.assertEqual(str(d), 'michael')