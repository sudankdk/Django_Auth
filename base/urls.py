
from django.urls import path
from .views import get_notes,CustomTokenObtainPairView,customRefreshTokenView,log_out,is_authenticated,register
urlpatterns = [
   
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', customRefreshTokenView.as_view(), name='token_refresh'),
    path('notes/', get_notes),
    path('logout/',log_out),
    path('authenticated/',is_authenticated),
    path('register/',register),
   
]