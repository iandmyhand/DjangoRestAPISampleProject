from django.test import TestCase

from ping.models import Ping


# python3 manage.py makemigrations --settings=www.settings.test ping
class TestPing(TestCase):

    def setUp(self):
        Ping.objects.create(test=1)

    def test_ping(self):
        _ping = Ping.objects.get(test=1)
        self.assertEqual(1, _ping.test)
