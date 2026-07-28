from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet, BranchViewSet, SectorViewSet,
    TicketTypeViewSet, TicketSubtypeViewSet,
)

router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='company')
router.register('branches', BranchViewSet, basename='branch')
router.register('sectors', SectorViewSet, basename='sector')
router.register('ticket-types', TicketTypeViewSet, basename='ticket-type')
router.register('ticket-subtypes', TicketSubtypeViewSet, basename='ticket-subtype')

urlpatterns = router.urls