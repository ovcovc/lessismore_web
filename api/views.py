from rest_framework import viewsets
from api.serializers import InjurySerializer
from injuries.models import Injury

__author__ = 'Piotr'


class InjuryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Injury.objects.all()
    serializer_class = InjurySerializer