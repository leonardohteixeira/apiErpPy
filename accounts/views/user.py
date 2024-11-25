from accounts.views.base import Base
from accounts.models import User
from accounts.seriaizers import UserSeriaizer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class GetUser(Base):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        user = User.objects.filter(id=request.user.id).first()
        enterprise = self.get_enterprise_user(user)

        serializer = UserSeriaizer(user)

        return Response({
            "user": serializer.data,
            "enterprise": enterprise
        })