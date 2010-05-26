try:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'django-world',
    version = '0.1',
    packages = ['world', 'world.management', 'world.management.commands'],
    author = 'Vasil Vangelovski',
    author_email = 'vvangelovski@gmail.com',
    license = 'New BSD License (http://www.opensource.org/licenses/bsd-license.php)',
    description = 'Django geographic models and utilities for importing geographic datasets',
    long_description = 'A reusable Django application that provides models and utilities for importing various geographic datasets.',
    url = 'http://code.google.com/p/django-world/',
    download_url = 'http://code.google.com/p/django-world/downloads/list',
   
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
