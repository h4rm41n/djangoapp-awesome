from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index),
    # path('postdata/', IndexPost),
]
