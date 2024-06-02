from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(class)s_created_by', null=True, blank=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(class)s_last_modified_by', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class VehicleMake(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=50, unique=True)
    country = models.CharField(_("Country"), max_length=50)

    class Meta:
        verbose_name = _("Vehicle Make")
        verbose_name_plural = _("Vehicle Makes")

    def __str__(self):
        return self.name


class VehicleModel(TimeStampedModel):
    make = models.ForeignKey(VehicleMake, on_delete=models.CASCADE, verbose_name=_("Make"))
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = _("Vehicle Model")
        verbose_name_plural = _("Vehicle Models")
        unique_together = ('make', 'name')

    def __str__(self):
        return self.name

class VehicleType(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=50, unique=True)

    class Meta:
        verbose_name = _("Vehicle Type")
        verbose_name_plural = _("Vehicle Types")

    def __str__(self):
        return self.name

class VehicleEngineType(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=50, unique=True)

    class Meta:
        verbose_name = _("Vehicle Engine Type")
        verbose_name_plural = _("Vehicle Engine Types")

    def __str__(self):
        return self.name

class Vehicle(TimeStampedModel):
    TRANSMISSION_CHOICES = (
        ('A', 'Automatic'),
        ('M', 'Manual'),
    )

    serial_number = models.CharField(_("Serial Number"), max_length=17, unique=True)  
    vehicle_model = models.ForeignKey(VehicleModel, verbose_name=_("Model"), on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, verbose_name=_("Type"), on_delete=models.CASCADE)
    engine_type = models.ForeignKey(VehicleEngineType, verbose_name=_("Engine Type"), on_delete=models.CASCADE)
    color = models.CharField(_("Color"), max_length=50)
    transmission = models.CharField(_("Transmission"), max_length=1, choices=TRANSMISSION_CHOICES)
    purchase_date = models.DateField(_("Purchase Date"))

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Vehicle_detail", kwargs={"pk": self.pk})
