from unicodedata import name
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
urlpatterns = [

    path('', views.apiOverview, name='api-overview'),
    path('offers/', views.offersList, name='offers-list'),
    path('offer-detail/<str:pk>/', views.offerDetail, name="offer-detail"),
    path('offer-create/', views.offerCreate, name='offer-create'),
    path('offer-update/<str:pk>/', views.offerUpdate, name="offer-update"),
    path('offer-delete/<str:pk>/', views.offerDelete, name="offer-delete"),
    path('company-create/', views.companyCreate, name='company-create'),
    path('company-detail/<str:pk>/', views.companyDetail, name="company-detail"),
    path('proposal-detail/<str:id_company>/',
         views.proposalDetail, name="proposal-detail"),
    path('choose-offer/<str:id_company>/',
         views.chooseOffer, name="choose-offer"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
