from typing import Any
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from . models import VehicleMake, VehicleModel, VehicleType, VehicleEngineType, Vehicle


class VehicleMakeResource(resources.ModelResource):
    class Meta:
        model = VehicleMake


@admin.register(VehicleMake)
class VehicleMakeAdmin(ImportExportModelAdmin):
    """
    ModelAdmin is very flexible. It has several options for dealing with customizing the interface
    """
    resource_classes = [VehicleMakeResource] # This will allow the model to be exported and imported
    list_display = ['name', 'country','created_at','modified_at'] #This will display the fields in the list view
    # date_hierarchy = "created_at" This will include a date-based drilldown navigation by the field.
    # exclude = ['created_by'] This excludes the field from the change/create form
    # fields = [('name','country'),'created_by','last_modified_by'] Alternatively only the fields that will be present in the form 
    fieldsets = [
        ('Vehicle Make', {'fields': ['name', 'country']}),
        ('User', {'fields': ['created_by', 'last_modified_by']})
    ] # This will group the fields in the form
    search_fields = ['name','country'] # This will add a search box to the list view
    list_filter = ['country'] # This will add a filter to the list view
    ordering = ['name'] # This will order the list view by the field
    readonly_fields = ['created_by', 'last_modified_by'] # This will make the fields read-only in the form

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not obj.pk:
            obj.created_by = request.user
        obj.last_modified_by = request.user
        return super().save_model(request, obj, form, change)


class VehicleModelResource(resources.ModelResource):
    class Meta:
        model = VehicleModel

@admin.register(VehicleModel)
class VehicleModelAdmin(ImportExportModelAdmin):
    resource_classes = [VehicleModelResource]
    list_display = ['make', 'name','created_at','modified_at']
    fieldsets = [
        ('Vehicle Model', {'fields': ['make', 'name']}),
        ('User', {'fields': ['created_by', 'last_modified_by']})
    ]
    search_fields = ['name','make__name'] # __ allows searching by related fields
    list_filter = ['make']
    ordering = ['name']
    readonly_fields = ['created_by', 'last_modified_by']

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not obj.pk:
            obj.created_by = request.user
        obj.last_modified_by = request.user
        return super().save_model(request, obj, form, change)


class VehicleTypeResource(resources.ModelResource):
    class Meta:
        model = VehicleType

@admin.register(VehicleType)
class VehicleTypeAdmin(ImportExportModelAdmin):
    resource_classes = [VehicleTypeResource]
    list_display = ['name','created_at','modified_at']
    fieldsets = [
        ('Vehicle Type', {'fields': ['name']}),
        ('User', {'fields': ['created_by', 'last_modified_by']})
    ]
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = ['created_by', 'last_modified_by']

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not obj.pk:
            obj.created_by = request.user
        obj.last_modified_by = request.user
        return super().save_model(request, obj, form, change)
    

class VehicleEngineResource(resources.ModelResource):
    class Meta:
        model = VehicleEngineType

@admin.register(VehicleEngineType)
class VehicleEngineTypeAdmin(ImportExportModelAdmin):
    resource_classes = [VehicleEngineResource]
    list_display = ['name']
    fieldsets = [
        ('Vehicle Engine Type', {'fields': ['name']}),
        ('User', {'fields': ['created_by', 'last_modified_by']})
    ]
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = ['created_by', 'last_modified_by']

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not obj.pk:
            obj.created_by = request.user
        obj.last_modified_by = request.user
        return super().save_model(request, obj, form, change)

class VehicleResource(resources.ModelResource):
    class Meta:
        model = Vehicle

@admin.register(Vehicle)
class VehicleAdmin(ImportExportModelAdmin):
    resource_classes = [VehicleResource]
    list_display = ['id','vehicle_model', 'serial_number','vehicle_make','vehicle_type','color','transmission','engine_type','created_at','modified_at']
    fieldsets = [
        ('Vehicle', {'fields': ['vehicle_model', 'serial_number','vehicle_type','purchase_date']}),
        ('Details', {'fields': ['color', 'transmission', 'engine_type']}),
        ('User', {'fields': ['created_by', 'last_modified_by']})
    ]
    search_fields = ['vehicle_model__name','serial_number','vehicle_type__name']
    list_filter = ['vehicle_model','vehicle_type','transmission','engine_type']
    ordering = ['vehicle_model','serial_number']
    readonly_fields = ['created_by', 'last_modified_by']

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not obj.pk:
            obj.created_by = request.user
        obj.last_modified_by = request.user
        return super().save_model(request, obj, form, change)

    def vehicle_make(self, obj):
        return obj.vehicle_model.make.name
    
    vehicle_make.short_description = 'Make'