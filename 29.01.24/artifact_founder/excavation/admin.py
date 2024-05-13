from django.contrib import admin
from excavation.models import ExcavationSite, Artifact
# Register your models here.

admin.site.register([
    ExcavationSite,
    Artifact,
])