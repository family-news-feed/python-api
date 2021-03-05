from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework import permissions


from db.models import *
from db.serializers import *


class GuardianViewSet(ModelViewSet):
    serializer_class = GuardianSerializer
    queryset = Guardian.objects.all()


class PatientViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class ApprovedGuardianEventViewSet(ModelViewSet):
    serializer_class = ApprovedGuardianEventSerializer
    queryset = ApprovedGuardianEvent.objects.all()


class ApprovedPatientEventViewSet(ModelViewSet):
    serializer_class = ApprovedPatientEventSerializer
    queryset = ApprovedPatientEvent.objects.all()


class GuardianNotificationInstanceViewSet(ModelViewSet):
    serializer_class = GuardianNotificationInstanceSerializer
    queryset = GuardianNotificationInstance.objects.all()


class GuardianPatientPairViewSet(ModelViewSet):
    serializer_class = GuardianPatientPairSerializer
    queryset = GuardianPatientPair.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]