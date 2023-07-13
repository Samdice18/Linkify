import importlib, subprocess, os

class InstallModules:
    def install_module(module_name):
        try:
            importlib.import_module(module_name)
        except ImportError:
            with open(os.devnull, 'w') as devnull:
                subprocess.check_call(['pip', 'install', module_name], stdout=devnull, stderr=devnull)
                