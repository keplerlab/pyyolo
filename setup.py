from distutils.core import setup, Extension
import numpy

DEFAULT_EXTENSION_KWARGS = {
    "extra_compile_args": ["-w"]
}

def pyx_extension(**kwargs):
    for key, value in DEFAULT_EXTENSION_KWARGS.items():
        if key not in kwargs:
            kwargs[key] = value

    return Extension(**kwargs)

module = Extension('pyyolo',
	library_dirs=['.'],
	libraries=['yolo'],
	include_dirs=[numpy.get_include(), './darknet/include'],
	extra_compile_args=['-w'],
	sources = ['module.c'])


setup (name = 'pyyolo',
	version = '0.1',
	description = 'YOLO wrapper',
	ext_modules = [module])
