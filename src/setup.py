from setuptools import setup


def readme():
	with open('README.rst') as f:
		return f.read()


setup(name='jk_commentjson',
	version='0.2016.16',
	description='An improved version of https://pypi.python.org/pypi/commentjson/',
	url='',
	author='Jürgen Knauth',
	author_email='jk@binary-overflow.de',
	license='MIT',
	packages=['jk_commentjson'],
	install_requires=[
	],
	include_package_data=True,
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Programming Language :: Python :: 3.5',
	],
	long_description=readme(),
	zip_safe=False)

