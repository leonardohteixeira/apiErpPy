from accounts.views.base import Base
from accounts.auth import Authentication
from accounts.seriaizers import UserSeriaizer

from rest_framework.response import Response

class Signup(Base):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        user = Authentication.signup(self, name=name, email=email, password=password)

        serializer = UserSeriaizer(user)

        return Response({"user": serializer.data})