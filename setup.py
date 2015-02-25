import os

from setuptools import setup, find_packages

setup(
    name='sql_novice_survey',
    version="0.0.1",
    description='First encounter with SQL using the Antarctic survey data as an example.',
    license='CC BY 4.0',
    author='Software Carpentry',
    packages=find_packages(),
    package_dir={"sql_novice_survey":"."},
    #package_data={"sql_novice_survey":["*.dll","*.pyd"]},
    zip_safe=False,
    requires=["commonmark", "pandocfilters", "pyyaml"],
    entry_points={
        'console_scripts': [
            'sql_novice_survey = sql_novice_survey.main:main'
        ]
    }
)
