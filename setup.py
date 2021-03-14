from setuptools import setup, find_packages
setup(name = 'django_listfield',
version = '0.1',
description = 'Add listfield for Django model and form',
url = '#',
author = 'Weilu Wang',
author_email = 'wandawwl@gmail.com',
license = 'MIT',
packages = ['listfield', ],
package_data = {
	'listfield': ['templates/*.html',]
},
include_package_data = True,
zip_safe = False,
install_requires = ['django>=3.0',],
keywords = ['python', 'django', 'listfield'])