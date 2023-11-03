from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account



class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message='A user with that username already exists.',
            )
        ],
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message= "user with this email already exists.",
            )
        ],
    )

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_superuser"
        ]
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self,validated_data):
        if validated_data["is_superuser"] == True:
            account = Account.objects.create_superuser(**validated_data)
        else:
            account = Account.objects.create_user(**validated_data)
        return account

