import subprocess
import tempfile
import os


class GSLWrapper(object):

    def __init__(self, settings):
        self.settings = settings

    def compile(self, gsl_input_str):
        compiler_inputs = self._generate_input_files(gsl_input_str)

        self._run_compiler(
            compiler_inputs['input_file'],
            compiler_inputs['working_dir'])

        return compiler_inputs

    def _generate_input_files(self, gsl_input_str):
        working_path = self.settings.get('working_path', None)
        temp_dir_path = tempfile.mkdtemp(dir=working_path)

        gsl_file_path = '{}/input.gsl'.format(temp_dir_path)

        with open(gsl_file_path, 'w+') as input_fp:
            input_fp.write(gsl_input_str)

        return {
            'working_dir': temp_dir_path,
            'input_file': gsl_file_path
        }

    def _run_compiler(self, input_file_path, output_directory):
        gsl_compiler_path = self.settings['gsl_compiler_path']
        cwd_path = self.settings['gsl_base_path']

        output_json_path = '{}/output.json'.format(output_directory)
        stdout_path = '{}/stdout.txt'.format(output_directory)
        stderr_path = '{}/stderr.txt'.format(output_directory)

        args = [
            'mono',
            gsl_compiler_path,
            input_file_path,
            '--json',
            output_json_path
        ]

        stdout_fp = open(stdout_path, 'w+')
        stderr_fp = open(stderr_path, 'w+')

        result = subprocess.Popen(
            args,
            stdout=stdout_fp,
            stderr=stderr_fp,
            cwd=cwd_path)

        stdout_fp.close()
        stderr_fp.close()

        return result

    def list_reference_genomes(self):
        working_path = self.settings.get('gsl_base_path', None)
        gslc_lib_path = working_path + '/gslc_lib'
        return [
            name
            for name in os.listdir(gslc_lib_path)
            if os.path.isdir(os.path.join(gslc_lib_path, name))
        ]
