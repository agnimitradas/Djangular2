from rest_framework import routers

from main import views

router = routers.DefaultRouter()
router.register(r'all', views.EventsView)

urlpatterns = router.urls