from django.urls import path
from .views import IndexView, CreateClienteView, UpdateClienteView, DeleteClienteView, ClienteDetailView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateClienteView.as_view(), name='add_cliente'),
    path('<int:pk>/update/', UpdateClienteView.as_view(), name='upd_cliente'),
    path('<int:pk>/delete/', DeleteClienteView.as_view(), name='del_cliente'),
    path('<int:pk>/detail/', ClienteDetailView.as_view(), name='detail_cliente'),
]