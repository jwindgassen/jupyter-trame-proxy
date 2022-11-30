from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

version='0.1.0'
setup(
    name = 'jupyter-trame-proxy',
    version = version,
    packages = find_packages(),

    url = 'https://github.com/jwindgassen/jupyter-trame-proxy',
    download_url = 'https://github.com/jwindgassen/jupyter-trame-proxy/archive/v{0}.tar.gz'.format(version),

    author = 'Jonathan Windgassen',
    author_email = 'j.windgassen@fz-juelich.de',

    description = 'ParaView trame proxy for JupyterLab',
    long_description = long_description,
    long_description_content_type = 'text/markdown',

    keywords = ['jupyter', 'trame', 'paraview', 'jupyterhub', 'jupyter-server-proxy'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Jupyter',
    ],

    entry_points = {
        'jupyter_serverproxy_servers': [
            'trame = jupyter_trame_proxy:setup_trame',
        ]
    },
    python_requires = '>=3.9',
    install_requires = ['jupyter-server-proxy>=3.1.0'],
    include_package_data = True,
    zip_safe = False
)
