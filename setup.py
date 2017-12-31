from setuptools import setup

setup(
    name='cc_test_module',
    version='0.0.1',
    description='a pip-installable package for testing concourse pipelines',
    license='MIT',
    author='David Ohlemacher',
    author_email='ohlemacher@ieee.org',
    keywords=['concourse', 'test'],
    url='https://github.com/ohlemacher/cc_test_module',

	classifiers = ['Development Status :: 3 - Alpha',
				   'Programming Language :: Python :: 3.6',
                   'Intended Audience :: Developers']
)
