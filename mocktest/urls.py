from rest_framework.routers import DefaultRouter
from .views import BotUsersViewset
from teacher.views import FanTestView,BlokTestlarView
from django.urls import path,include
router = DefaultRouter()
router.register('newuser',BotUsersViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('fantest/<str:test_kodi>/<str:tel>/',FanTestView.as_view()),
    path('bloktest/<str:test_kodi>/<str:tel>/', BlokTestlarView.as_view())
]
