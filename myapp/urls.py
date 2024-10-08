from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('list-task/', ListTasksView.as_view(), name = 'list-task'),
    path('create-task/', CreateTaskView.as_view(), name = 'create-task'),
    path('update-task/<int:pk>/', UpdateTaskView.as_view(), name = 'update-task'),
    path('todo/', TodoView.as_view(), name = "list"),
]