#!/usr/bin/env python
"""
QuadHLFC - The High-Level Flight Controller for QuadCopter
Copyright (c) 2012 Greg Haynes

This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.command.install_scripts import install_scripts
from distutils.core import setup


class InstallScripts(install_scripts):
    '''create the bat for windows so the launcher script
    works out of the box'''
    def run(self):
        import os
        '''if os.name == 'nt':
            import sys
            parts = os.path.split(sys.executable)
            py_path = os.path.join(*(parts[:-1]))
            script_path = os.path.join(py_path, 'Scripts')
            f = open(os.path.join(script_path, 'pymazon.bat'), 'w')
            pymazon = os.path.join(script_path, 'pymazon')
            bat = '@' + ('"%s" "%s"' % (sys.executable, pymazon)) + ' %*'
            f.write(bat)
            f.close()'''
        install_scripts.run(self)


setup(name='QuadHLFC',
      version='1.12.0526',
      description='The High-Level Flight Controller for QuadCopter',
      author='Greg Haynes',
      author_email='psu-avt@googlegroups.com',
      url='https://github.com/PSU-AVT/QuadHLFC/tree/v4',
      package_dir = {'quadhlfc': './quadhlfc'},
      packages=['quadhlfc', 'quadhlfc.core','quadhlfc.resource'],
      package_data={'quadhlfc.resource': ['icons/*.png']},
      scripts=['./bin/quadhlfc'],
      license='GPLv3',
      long_description=\
'''The high level flight computer performs data aggregation on some sensors 
and the LLFC and provides a pub-sub interface for remote processes to 
acquire this data. It also acts as a control gateway for the quadcopter.''',
      cmdclass={'install_scripts': InstallScripts},
     )
