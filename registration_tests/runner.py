#!/usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'registration_tests.settings'
test_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, test_dir)

from django.conf import settings
from django.test import simple


def runtests(*test_args):
    if not test_args:
        test_args = ('registration_tests',)

    runner = simple.DjangoTestSuiteRunner(verbosity=1, interactive=True, failfast=False)
    failures = runner.run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
