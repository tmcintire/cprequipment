from django.conf.urls import include, url
from django.contrib import admin
from views import equipment, drivers_list, addservice, details, servicelog, addequipment, addtype, \
    editequipment, serviceview, editdriver, deletedriver, newservice, editservice, deleteservice, adddepartment, \
    adddriver, yearreport


urlpatterns = [
    url(r'^equipment/$', equipment, name="equipment"),
    url(r'^$', equipment, name="equipment"),
    url(r'^drivers/$', drivers_list, name="drivers"),
    url(r'^drivers/add/$', adddriver, name="adddriver"),
    url(r'^drivers/edit/(?P<driver_id>[0-9]+)/$', editdriver, name="editdriver"),
    url(r'^drivers/delete/(?P<driver_id>[0-9]+)/$', deletedriver, name="deletedriver"),
    url(r'^details/(?P<equipment_id>[0-9]+)/$', details, name="details"),
    url(r'^details/(?P<equipment_id>[0-9]+)/addservice/$', addservice, name="addservice"),
    url(r'^servicelog', servicelog, name="servicelog"),
    url(r'^service/(?P<service_id>[0-9]+)/$', serviceview, name="service"),
    url(r'^addservice/$', newservice, name='newservice'),
    url(r'^service/edit/(?P<service_id>[0-9]+)/$', editservice, name="editservice"),
    url(r'^service/delete/(?P<service_id>[0-9]+)/$', deleteservice, name="deleteservice"),
    url(r'^addequipment', addequipment, name="addequipment"),
    url(r'^equipment/edit/(?P<equipment_id>[0-9]+)/$', editequipment, name="editequipment"),
    url(r'^details/(?P<equipment_id>[0-9]+)/$', details, name="details"),
    url(r'^addtype', addtype, name="addtype"),
    url(r'^adddepartment', adddepartment, name="adddepartment"),
    url(r'^(?P<year>[0-9]{4})/$', yearreport, name='yearreport'),
]
