from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from emissions_project.infrastructure.repository_impl import EmissionRepositoryImpl
from emissions_project.infrastructure.serializers import EmissionSerializer
from emissions_project.usecases.get_emissions import GetEmissions


class EmissionListView(APIView):
    def get(self, request):
        filters = {}
        for key in ["country", "activity", "emission_type"]:
            if key in request.GET:
                filters[key] = request.GET[key]
        repo = EmissionRepositoryImpl()
        usecase = GetEmissions(repo)
        emissions = usecase.execute(filters)
        serializer = EmissionSerializer(emissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
