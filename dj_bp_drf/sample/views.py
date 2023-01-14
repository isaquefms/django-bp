from django.http import JsonResponse
from rest_framework.views import APIView


class HomeView(APIView):

    def get(self, request, format=None):
        return JsonResponse({"message": 'Hello World from Django and Docker'})
