from .models import Account
from .serializers import AccountSerializer
from rest_framework.generics import CreateAPIView
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView


class CreateAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @extend_schema(
            tags = ["Criação de usuário"] 
            )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

@extend_schema(
    tags = ["Autenticação"] 
    )
class LoginView(TokenObtainPairView):
    ...