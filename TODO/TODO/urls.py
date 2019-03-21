from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views


import TASK.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TASK.views.TaskList.as_view()),

    path('tasks/<int:pk>/', TASK.views.TaskDetails.as_view()),

    path('api-token-auth/', obtain_auth_token),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]