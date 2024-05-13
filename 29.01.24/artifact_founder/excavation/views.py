from django.shortcuts import render
from excavation.models import ExcavationSite, Artifact
from django.http import HttpRequest, HttpResponse
# Create your views here.


def sites_list(request):
    excavation_sites= ExcavationSite.objects.all()
    return render(request, 'sites_list.html', {'sites': excavation_sites})

def site_details(request:HttpRequest) -> HttpResponse:
    id = int(request.GET.get('id', '1'))
    site = ExcavationSite.objects.get(id=id)
    artifacts = Artifact.objects.filter(site=site)
    return render(request, 'site_artifacts.html', {'artifacts': artifacts, "site":site})