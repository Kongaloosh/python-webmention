from distutils.core import setup

setup(
    name="PythonWebmention",
    version=0.1,
    packages=['python_webmention'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().split('\n'),
)
