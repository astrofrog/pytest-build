import sys
import subprocess


def pytest_load_initial_conftests(args):
    if '--build-inplace' in args:
        subprocess.call([sys.executable, 'setup.py', 'build_ext', '--inplace'])
        args.remove('--build-inplace')
