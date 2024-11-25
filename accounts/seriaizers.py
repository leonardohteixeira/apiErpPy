from rest_framework import serializers

from accounts.models import User

class UserSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email'
        )