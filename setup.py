from setuptools import find_packages, setup

setup(
    name='demo',
    version='0.0.1',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
    ],
    extras_require={
        'dev': [
            "pytest-cov"
        ],
    },
    entry_points={
        'pytest11': [
            'pytest_demo=demo.plugin'
        ]
    },
    zip_safe=True
)
