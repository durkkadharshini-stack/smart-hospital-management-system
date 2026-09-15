from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorViewSet, AppointmentViewSet, TreatmentViewSet

router = DefaultRouter()

router.register('patients', PatientViewSet)
router.register('doctors', DoctorViewSet)
router.register('appointments', AppointmentViewSet)
router.register('treatments', TreatmentViewSet)

urlpatterns = router.urls