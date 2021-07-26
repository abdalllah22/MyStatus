from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):
        a7a = [
            'ahmed',
            'abdallah',
            'mohamed'
        ]
        return Response({
            'message':'hello',
            'list':a7a,
        })