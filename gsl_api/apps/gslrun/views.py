from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import CompilerRequestSerializer
from .wrapper import GSLWrapper


class GSLWrapperMixin(object):
    @property
    def gsl_wrapper(self):
        return GSLWrapper(settings.GSL_OPTIONS)


class CompileGSLView(APIView, GSLWrapperMixin):
    serializer_class = CompilerRequestSerializer

    def post(self, request):
        serializer = CompilerRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data['code']
        print(code)

        results = self.gsl_wrapper.compile(code)

        return Response({
            'code': code,
            'result': results
        }, status.HTTP_200_OK)


class ListReferenceGenomesView(APIView, GSLWrapperMixin):

    def get(self, request):
        genome_names = self.gsl_wrapper.list_reference_genomes()
        return Response({
            'results': genome_names
        }, status.HTTP_200_OK)
