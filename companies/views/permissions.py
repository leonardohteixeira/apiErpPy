from companies.views.base import Base
from companies.utils.permissions import GroupsPermission
from companies.serializers import PermissionsSerializer

from rest_framework.response import Response

from django.contrib.auth.models import Permission

class PermissionDetail(Base):
    permission_classes = [GroupsPermission]

    def get(self, request):
        permission = Permission.objects.filter(content_type_id__in=[2, 7, 11, 13]).all()

        serializer = PermissionsSerializer(permission, many=True)

        return Response({"permissions": serializer.data})