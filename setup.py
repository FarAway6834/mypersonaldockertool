from setuptools import setup, find_packages

setup(
    name='mypersonaldockeruse',
    version='0.0.1',
    description='using PyPI mydockertool package much better in docker by PyPI mypersonaldockeruse, and also it deploy as snap & apt with build-essential & python also deploy as docker 2 use much better.',
    author='du7ec',
    author_email='dutec6834@gmail.com',
    url='https://github.com/FarAway6834/mypersonaldockertool',
    packages=find_packages(exclude=[]),
    install_requires=['mydockeruse'],
    keywords=['mydockeruse', 'mypersonaldockeruse tool', 'mypersonaldockeruse'],
    python_requires='>=3.4',
    package_data={},
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
)