from setuptools import setup, Extension, find_packages
import sys

__author__ = "etseng@pacb.com"
__version__ = "2.4.0"


setup(
    name = 'CoSA',
    version=__version__,
    description='Coronavirus Sequence Analysis',
    author='Elizabeth Tseng',
    author_email='etseng@pacb.com',
    zip_safe=False,
    packages = ['cosa', 'cosa.io'],
    package_dir = {'cosa': 'cosa',
                   'cosa.io': 'cosa/io',
                   'cosa.pacbio': 'cosa/pacbio'},
    install_requires=[
        'biopython',
        ],
    scripts = ['cosa/clean_up_metadata.py',
               'cosa/filter_gappedshort.py',
			   'cosa/utils/fetch_NCBI.py',
               'cosa/utils/calculate_coverage_and_missing_bases.py',
               'cosa/utils/combine_demux_by_patient.py',
               'cosa/pacbio/subsample_amplicons.py',
               'cosa/pacbio/juliet_json_to_vcf.py',
               ],
    )
