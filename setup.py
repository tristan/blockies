from setuptools import setup

setup(
    name='blockies',
    version='0.0.2',
    author='Tristan King',
    author_email='tristan.king@gmail.com',
    py_modules=['blockies'],
    url='http://github.com/tristan/blockies',
    description='A tiny library for generating blocky identicons.',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read()
)
