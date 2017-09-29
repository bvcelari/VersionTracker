#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from versiontracker.serializers import UserSerializer, GroupSerializer, PackageSerializer, BundleSerializer, BuiltPackageSerializer, BuiltBundleSerializer
from versiontracker.models import Package, Bundle, BuiltPackage, BuiltBundle

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PackageViewSet(viewsets.ModelViewSet):
    """
    API endpoint will show the current list of Packages availables
    """
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class BundleViewSet(viewsets.ModelViewSet):
    """
    API endpoint will show the current list of Bundles availables
    """
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer

class BuiltPackageViewSet(viewsets.ModelViewSet):
    """
    API endpoint will show the current list of Packages built
    """
    queryset = BuiltPackage.objects.all()
    serializer_class = BuiltPackageSerializer

class BuiltBundleViewSet(viewsets.ModelViewSet):
    """
    API endpoint will show the current list of Bundles built
    """
    queryset = BuiltBundle.objects.all()
    serializer_class = BuiltBundleSerializer
