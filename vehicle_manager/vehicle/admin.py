from django.contrib import admin
from . models import VehicleMake, VehicleModel, VehicleType, VehicleEngineType, Vehicle


@admin.register(VehicleMake)
class VehicleMakeAdmin(admin.ModelAdmin):
    """
    ModelAdmin is very flexible. It has several options for dealing with customizing the interface
    """
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

@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ['make', 'name','created_at','modified_at']
    fieldsets = [
        ('Vehicle Model', {'fields': ['make', 'name']}),
        ('User', {'fields': ['created_by', 'last_modified_by']})
    ]
    search_fields = ['name','make__name'] # __ allows searching by related fields
    list_filter = ['make']
    ordering = ['name']
    readonly_fields = ['created_by', 'last_modified_by']

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name','created_at','modified_at']
    fieldsets = [
        ('Vehicle Type', {'fields': ['name']}),
        ('User', {'fields': ['created_by', 'last_modified_by']})
    ]
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = ['created_by', 'last_modified_by']

@admin.register(VehicleEngineType)
class VehicleEngineTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        ('Vehicle Engine Type', {'fields': ['name']}),
        ('User', {'fields': ['created_by', 'last_modified_by']})
    ]
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = ['created_by', 'last_modified_by']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_model', 'serial_number','vehicle_make','vehicle_type','color','transmission','engine_type','created_at','modified_at']
    fieldsets = [
        ('Vehicle', {'fields': ['vehicle_model', 'serial_number','vehicle_type','purchase_date']}),
        ('Details', {'fields': ['color', 'transmission', 'engine_type']}),
        ('User', {'fields': ['created_by', 'last_modified_by']})
    ]
    search_fields = ['vehicle_model__name','serial_number','vehicle_type__name']
    list_filter = ['vehicle_model','vehicle_type','transmission','engine_type']
    ordering = ['vehicle_model','serial_number']
    readonly_fields = ['created_by', 'last_modified_by']

    def vehicle_make(self, obj):
        return obj.vehicle_model.make.name
    
    vehicle_make.short_description = 'Make'