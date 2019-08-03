from .settings import *

ALLOWED_HOSTS = [
    '*',
]

GSL_OPTIONS = {
    'working_path': '/gsl-tmp-output',
    'gsl_base_path': '/app/Gslc', # folder containing gslc_lib
    'gsl_compiler_path': '/app/Gslc/bin/Gslc/Gslc.exe'
}
