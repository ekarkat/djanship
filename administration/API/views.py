from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import StateSerializer, CitySerializer
from administration.models import State, City


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
    http_method_names = ['get']

    # add a custom action to get the cities of a state
    @action(detail=True, methods=['get'], url_path='cities', url_name='state_cities')
    def get_cities(self, request, pk=None):
        try:
            state = self.get_object()  # This will get the State instance based on the pk in the URL
        except State.DoesNotExist:
            return Response({"error": "State not found"}, status=404)

        cities = City.objects.filter(state=state)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    http_method_names = ['get']
