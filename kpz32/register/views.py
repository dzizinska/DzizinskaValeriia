from django.shortcuts import render
from django.http import HttpResponse
import datetime
from models import *
def update(request):
    '''Licence.objects.create(series = '6432',issue_date = datetime.date(2012,4,12),company_id =
                           Company.objects.create (company_n = 'Hoking',address =  'Kyiv',registration =  '1003003',
                                                   specification =  'Save Program',
                                                   owner_id = Owner.objects.create(owner_n = 'Ben Kingsli',
                                                                                   form_of_ownership = 'Limited Liability',
                                                                                   owner_type = 'Individual') ))'''

    #Up('lll', 'blabla')
    ShowCompany()

    return comp(request)


def comp(request):
    comp_list = Company.objects.order_by('company_n')[:5]
    context = {'comp_list': comp_list}
    return render(request, 'reestr/comp.html', context)




