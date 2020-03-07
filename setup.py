# -*- coding: utf-8 -*-

from os.path import join, dirname

from setuptools import setup, find_packages

import cube

setup(
        name="cube",
        version=cube.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),
        install_requires=["PyQt5", "pyaml"],
        entry_points={
            'gui_scripts':
                ['cube = cube.run:main']
        }

)
