import datetime

from django.utils import timezone
from django.test import TestCase

from .models import *


class LicenseMethodTests(TestCase):

    def test_licence_future_valid(self):

        time = timezone.now() - datetime.timedelta(days=30)
        future_license = Licence(issue_date=time)
        self.assertEqual(future_license.licence_valid(), False)

class ManageTest(TestCase):
    def setUp(self):
        self.licence = Licence.objects.create(series = '6432',issue_date = datetime.date(2012,4,12),company_id =
                           Company.objects.create (company_n = 'Hoking',address =  'Kyiv',registration =  '1003003',
                                                   specification =  'Save Program',
                                                   owner_id = Owner.objects.create(owner_n = 'Ben Kingsli',
                                                                                   form_of_ownership = 'Limited Liability',
                                                                                   owner_type = 'Individual') ))
    def test_create(self):
        self.assertEqual(self.licence.series, '6432')

    def test_select(self):
        licence = Licence.objects.get(series = '643')
        self.assertEqual(self.licence, licence)

    def test_update(self):
        self.licence.series = '5211'
        self.licence.save()
        licence = Licence.objects.get(series = '5211')
        self.assertEqual(self.licence, licence)

    def test_delete(self):
        self.licence.delete()
        licence = None
        try:
            licence = Licence.objects.get(series = '5211')
	except:
            self.assertEqual(licence, None)



