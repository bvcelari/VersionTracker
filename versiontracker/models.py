from __future__ import unicode_literals
import datetime

from django.contrib.auth.models import Group, User
from django.db import models

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class BuiltPackage(models.Model):
    name = models.CharField(max_length=200) # you can provide names like.. staging-branchA or similar
    package_list = models.ForeignKey(Package) # generated once that you request a new built package
    created = models.DateTimeField(default = datetime.datetime.now())
    requested_by = models.ForeignKey(User)
    def __unicode__(self):
        return self.name

class Bundle(models.Model):
    name = models.CharField(max_length=200) # name the colection of software that you want to handle together
    bundle_content =  models.ManyToManyField(Package) # will provide a list of packages that make this bundle
    def __unicode__(self):
        return self.name

class BuiltBundle(models.Model):
    name = models.CharField(max_length=200) # cool name for you bundle, like... fix the errors for bug-ABC 
    bundle_list = models.ManyToManyField(BuiltPackage) # generated once that you request the list of last packages built
    #created = models.DateTimeField(default = datetime.datetime.now()
    #user = models.OneToOneField(User)
    def __unicode__(self):
        return self.name

    
