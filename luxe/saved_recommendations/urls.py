from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('saved-recommendations/', views.SavedRecommendationList.as_view()),
    path('saved-recommendations/<int:pk>', views.SavedRecommendationDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)