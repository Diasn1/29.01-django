from django.urls import path
from excavation.views import sites_list, site_details

urlpatterns = [
    path('sites/', sites_list, name='sites_list'),
    path('sites/site/', site_details, name='site_details'),
        
]
