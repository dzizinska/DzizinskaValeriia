from django.db import models

from django.utils import timezone
import datetime
# Create your models here.


class Owner(models.Model):
    owner_n = models.CharField('name',max_length=200)
    form_of_ownership = models.CharField(max_length=200)
    owner_type = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return '{0} - {1},{2}'.format(self.owner_n,self.form_of_ownership,self.owner_type)

class ResponsiblePersons(models.Model):
    person_n = models.CharField('name',max_length=200)
    passport_code = models.IntegerField()
    id_code = models.IntegerField()
    #company_id = models.ForeignKey(Company,null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return '{0} - {1}'.format(self.person_n,self.passport_code)

class Company(models.Model):
    company_n = models.CharField('name',max_length=200)
    address = models.CharField(max_length=200)
    registration = models.BigIntegerField()
    specification = models.CharField(max_length=200)
    owner_id= models.ForeignKey(Owner)
    responpers_id=models.ForeignKey(ResponsiblePersons,null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return '{0} - {1},{2}'.format(self.company_n,self.address,self.specification)



class Licence(models.Model):
    series = models.CharField(max_length=200)
    issue_date = models.DateField()
    company_id = models.OneToOneField(Company,primary_key=True)
    def licence_valid(self):
        return self.issue_date >= timezone.now()
    licence_valid.admin_order_field = 'lic_date'
    licence_valid.boolean = True
    licence_valid.short_description = 'License valid?'

    def __unicode__(self):              # __unicode__ on Python 2
        return '{0} - {1},{2}'.format(self.series,self.issue_date,self.company_id)
'''
def Set():
    Licence.objects.create(series = '6432',issue_date = datetime.date(2012,4,12),company_id =
                           Company.objects.create (company_n = 'Hoking',address =  'Kyiv',registration =  '1003003',
                                                   specification =  'Save Program',
                                                   owner_id = Owner.objects.create(owner_n = 'Ben Kingsli',
                                                                                   form_of_ownership = 'Limited Liability',
                                                                                   owner_type = 'Individual') ))




def ShowCompany():
    print "Companies:"
    for company in Company.objects.all():
        print "Company name: %s, Address: %s, Registration: %s" % (company.company_n, company.address, company.registration)




def Up(update, replace):

    try:
       c = Company.objects.get(company_n = update)
       print 'Previous state:'
       ShowCompany()
       c.company_n = replace
       c.save()

    except:
        print 'Current state:'
        ShowCompany()

def ClearAll():
    Licence.objects.all().delete()


Up('Company1', 'Company2')'''





