from django.urls import path

from home.views import (
    index_view,
    LogoutView,
    LoginView,
    RegisterView,  # Añadir esta línea al final de la lista de URLs de la app home.py.
)

urlpatterns = [
    path(route='',view=index_view, name='index'),
    path(route='login/', view=LoginView.as_view(), name='login'),
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
    path(route='register/', view=RegisterView.as_view(), name='register')
]