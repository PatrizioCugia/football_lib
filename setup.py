from setuptools import setup, find_packages

setup(
    name='football_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scikit-learn',
        'scipy'
    ],
    author='Patrizio Cugia',
    author_email='your_email@example.com',
    description='A library for football player statistics and PCA analysis',
    url='https://github.com/PatrizioCugia/football_lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
