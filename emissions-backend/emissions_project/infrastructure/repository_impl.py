from emissions_project.domain.repositories import EmissionRepository
from emissions_project.infrastructure.models import EmissionModel


class EmissionRepositoryImpl(EmissionRepository):
    def list(self, filters=None):
        queryset = EmissionModel.objects.all()
        if filters:
            queryset = queryset.filter(**filters)
        return list(queryset)
