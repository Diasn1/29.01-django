from django.db import models

# Create your models here.


class ExcavationSite(models.Model):
    name = models.CharField(max_length=100, null=True)
    
    class Meta:
        app_label = "excavation"
    def __str__(self) -> str:
        return self.name


class Artifact(models.Model):
    name = models.CharField(max_length=100, null=True)
    found = models.DateTimeField(auto_now=True)
    site = models.ForeignKey('ExcavationSite', on_delete=models.CASCADE)

    class Meta:
        app_label = "excavation"
    def __str__(self) -> str:
        return self.name