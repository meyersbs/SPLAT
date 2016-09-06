from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='SPLAT',
    version='0.1.0',
    description='Speech Processing & Linguistic Analysis Tool',
    long_description=readme,
    author='Benjamin S. Meyers',
    author_email='ben@splat-library.org',
    maintainer='Benjamin S. Meyers',
    maintainer_email='ben@splat-library.org',
    url='http://splat-library.org',
    download_url='https://github.com/meyersbs/SPLAT/tarball/0.1.0',
    license=license,
    packages=['splat', 'splat.annotation', 'splat.base', 'splat.classify', 'splat.complexity', 'splat.corpus', 'splat.model', 'splat.parse', 'splat.sentenizers', 'splat.tag', 'splat.tokenizers']
)
