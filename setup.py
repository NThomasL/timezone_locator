from setuptools import setup

setup(
    name='timezone_locator',
    version='0.1',
    author='Nils Thomas Loefgren',
    author_email='nt.lofgren@gmail.com',
    long_description='Package for finding timezone of given coordinates',
    packages=['timezone_locator'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Fiona']
)