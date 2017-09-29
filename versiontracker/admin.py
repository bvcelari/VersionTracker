from django.contrib import admin

from versiontracker.models import Package, BuiltPackage, Bundle, BuiltBundle

class PackageAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id', 'name')

#this should be read only in the admin interface
class BuiltPackageAdmin(admin.ModelAdmin):
    fields = ['name','package_list','requested_by','created']
    list_display = ('id', 'name')

class BundleAdmin(admin.ModelAdmin):
    fields = ['name','bundle_content']
    list_display = ('id', 'name')

#this should be read only in the admin interface
class BuiltBundleAdmin(admin.ModelAdmin):
    fields = ['name','bundle_list']
    list_display = ('id', 'name')


admin.site.register(Package, PackageAdmin)
admin.site.register(BuiltPackage, BuiltPackageAdmin)
admin.site.register(Bundle, BundleAdmin)
admin.site.register(BuiltBundle, BuiltBundleAdmin)

