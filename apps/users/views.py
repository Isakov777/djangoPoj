from argparse import Action
from django.http import request
from django.shortcuts import render
from rest_framework import viewsets, generics
from apps.users.models import User
from apps.users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, IsAuthenticated
from apps.users.permissions import  IsOwner



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ IsOwner]

    # def get_permissions(self):
    #     self.permission_classes = [IsSuperUser]

    #     if self.action == 'retrieve':
    #        self.permission_classes = [IsOwner]
    #     return super(self.__class__, self).get_permissions()



        


    # def get_queryset(self):
    #     owner_queryset = self.queryset.filter(username = self.request.user)
    #     return owner_queryset
