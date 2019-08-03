from django.conf.urls import url
from .views import (
    CompileGSLView,
    ListReferenceGenomesView
)

app_name = 'gslrun'
urlpatterns = [
    url(
        r'compile/',
        CompileGSLView.as_view(),
        name='compile_gsl'
    ),
    url(
        r'list_genomes',
        ListReferenceGenomesView.as_view(),
        name='list_reference_genomes'
    )
]
