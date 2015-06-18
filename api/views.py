import random
import string
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import InjurySerializer
from injuries.models import Injury

__author__ = 'Piotr'

def token_generator(size=24, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@api_view(['GET', 'POST'])
def injury_list(request):
    """
    List all Injuries, or create a new Injury.
    """
    if request.method == 'GET':
        orders = Injury.objects.all()
        serializer = InjurySerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InjurySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
