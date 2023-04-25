from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'rule'
router = routers.DefaultRouter()
router.register(r'case', views.CaseViewSet, basename='case')
router.register(r'rule', views.ItemViewSet, basename='rule')
router.register(r'match', views.MatchViewSet, basename='match')

urlpatterns = [
    path('', include(router.urls)),
    path('rule_match', views.RuleMatch.as_view()),
]