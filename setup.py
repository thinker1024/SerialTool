import codecs
from setuptools import setup


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="SerialTool",
    version="0.0.7",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description='A tool for serial port debug usage',
    author='Tao Yang',
    author_email='yangtao.now@gmail.com',
    url='https://github.com/logself1988/SerialTool',
    packages=['SerialTool'],
    package_data={
        'SerialTool': ['README.rst', 'LICENSE']
    },
    install_requires=['pySerial'],
    entry_points="""
    [console_scripts]
    SerialTool = SerialTool.SerialPy:main
    """,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)
