from setuptools import setup, find_packages

setup(
    name = "django_il",
    version = "0.1",
    url = 'http://www.mksoft.co.il',
    license = 'N/A',
    description = "django.org.il webseite.",
    author = 'Meir Kriheli',
    author_email = 'meir@mksoft.co.il',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
    zip_safe = False
)
