from setuptools import setup, find_packages

from helga_spook import __version__ as version

setup(name='helga-spook',
      version=version,
      description=('prints nsa buzzwords'),
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Communications :: Chat :: Internet Relay Chat'],
      keywords='irc bot nsa spook emacs',
      author='Michael Orr',
      author_email='michael@orr.co',
      url='https://github.com/michaelorr/helga-spook',
      license='LICENSE',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['helga_spook.plugin'],
      zip_safe=True,
      entry_points = dict(
          helga_plugins=[
              'spook = helga_spook.plugin:spook',
          ],
      ),
)
