from distutils.core import setup
import glob
setup(name='blog',
      version='1.0',
      description='ghost blog',
      author='ghost',
      author_email='17366923916@163.com',
      url='www.ghost.com.cn',
      packages=['blog','post','user'],
      py_modules=['ghost'],
      data_files=glob.glob('templates/*.html')+['requirements','manage.py'])