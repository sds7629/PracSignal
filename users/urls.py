from rest_framework import routers
from . import views

app_name = "users"
router = routers.SimpleRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = []

urlpatterns += router.urls
