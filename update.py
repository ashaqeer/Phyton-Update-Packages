import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip3 install --upgrade --use-deprecated=legacy-resolver --no-warn-script-location " + ' '.join(packages), shell=True)