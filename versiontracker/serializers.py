from django.contrib.auth.models import User, Group
from rest_framework import serializers

from versiontracker.models import Package, Bundle, BuiltPackage, BuiltBundle


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('id','name')

class BundleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bundle
        fields = ('id','name')

class BuiltPackageSerializer(serializers.HyperlinkedModelSerializer):
    requested_by = serializers.ReadOnlyField(source='user.username')
    created = serializers.ReadOnlyField(source='notsurewhat')
    class Meta:
        model = BuiltPackage
        fields = ('name','package_list','requested_by','created')

class BuiltBundleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuiltBundle
        fields = ('name','bundle_list')

