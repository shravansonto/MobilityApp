# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, PlanViewSet
app_name='customer'
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'plans', PlanViewSet)
from .views import renew_plan, upgrade_downgrade_plan


urlpatterns = [
    path('', include(router.urls)),
    path('renew-plan/', renew_plan, name='renew-plan'),
    path('upgrade-downgrade-plan/', upgrade_downgrade_plan, name='upgrade-downgrade-plan'),
]
