from django.urls import path


from apps.users.views import RegisterView, UserAPIViewSet


urlpatterns = [
    path('', UserAPIViewSet.as_view({'get': 'list'})),
    path('<int:pk>', UserAPIViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('register/', RegisterView.as_view(), name='auth_register'),
]


