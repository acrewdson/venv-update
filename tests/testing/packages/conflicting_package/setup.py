from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import setup


setup(
    name=str('conflicting_package'),
    version='1',
    install_requires=[
        'many_versions_package<2',
    ],
    options={
        'bdist_wheel': {
            'universal': 1,
        }
    },
)  # pylint:disable=duplicate-code
