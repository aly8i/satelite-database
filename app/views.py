from .models import Account
from .serializers import AccountSerializer
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User

class AccountViewset(viewsets.ModelViewSet):    
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=(TokenAuthentication,)

class UserViewset (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

