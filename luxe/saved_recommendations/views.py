
# from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import SavedRecommendation
from .serializers import SavedRecommendationSerializer

# Create your views here.

class SavedRecommendationList(APIView):
    
    def get(self, request):
        saved_recommendations = SavedRecommendation.objects.all()
        serializer = SavedRecommendationSerializer(saved_recommendations, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = SavedRecommendationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
            )
        
class SavedRecommendationDetail(APIView):

    def get_object(self, pk):
        try:
            return SavedRecommendation.objects.get(pk=pk)
        except SavedRecommendation.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        saved_recommendations = self.get_object(pk)
        serializer = SavedRecommendationSerializer(saved_recommendations)
        return Response(serializer.data)

    def put(self, request, pk):
        saved_recommendations = self.get_object(pk)
        data = request.data
        serializer = SavedRecommendationSerializer(
            instance=saved_recommendations,data=data,partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        saved_recommendations = self.get_object(pk)
        saved_recommendations.delete()
        return Response({"detail": "Recommendation deleted"})