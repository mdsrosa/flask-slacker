"""
Flask-Slacker
--------------

Adds Slack support to your Flask application using Slacker.
"""
import ast
import re

from setuptools import setup


def get_version():
    _version_re = re.compile(r'__version__\s+=\s+(.*)')

    with open('flask_slacker/__init__.py', 'rb') as f:
        version = str(ast.literal_eval(_version_re.search(
            f.read().decode('utf-8')).group(1)))
        return version


install_requires = [
    'Flask >= 0.12.2',
    'Slacker >= 0.9.60'
]

test_requires = [
    'pytest >= 3.2.2',
    'pytest-runner >= 2.12.1',
    'pytest-flake8 >= 0.8.1',
    'pytest-isort >= 0.1.0'
]


setup(
    name='Flask-Slacker',
    version=get_version(),
    license='MIT',
    url='https://github.com/mdsrosa/flask-slacker',
    author='Matheus Rosa',
    author_email='matheusdsrosa@gmail.com',
    description='Adds support to your Flask application using Slacker.',
    long_description=__doc__,
    packages=['flask_slacker'],
    zip_safe=False,
    platforms='any',
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=test_requires,
    tests_require=test_requires,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
