#!/usr/bin/env python

from setuptools import setup
import aperture_contour.__init__ as meta

__name__ = "aperture_contour"
__install_requires__ = ["numpy"]

setup(name=__name__,
      version=meta.__version__,
      description=meta.__description__,
      author=meta.__author__,
      author_email=meta.__author_email__,
      url=meta.__url__,
      packages=["aperture_contour"],
      # package_dir={"": "aperture_contour"},
      install_requires=__install_requires__,
      zip_safe=False,
     )
