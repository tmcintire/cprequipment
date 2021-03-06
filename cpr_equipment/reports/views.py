from django.shortcuts import render
from django.db.models import Sum
from equipment.models import Equipment, Service
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def report(request):

    total = Service.objects.aggregate(Sum('cost')).values()[0]
    equipment = Equipment.objects.all()
    cemetery = Equipment.objects.filter(department=1).aggregate(Sum('service__cost')).values()[0]
    recreation = Equipment.objects.filter(department=3).aggregate(Sum('service__cost')).values()[0]
    other = Equipment.objects.filter(department=None).aggregate(Sum('service__cost')).values()[0]
    services = Service.objects.filter(service_date__year=2014)

    return render(request, 'reports.html', locals())
