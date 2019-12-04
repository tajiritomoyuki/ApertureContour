#!/usr/bin/env python

from distutils.core import setup

name = "aperture_contour"
version = "1.0"
description = "draw aperture contours"
author = "Tomoyuki Tajiri"
url = "https://github.com/tajiritomoyuki/aperture_contour"
install_requires = ["numpy"]

setup(name=NAME,
      version=version,
      description=description,
      author=author,
      author_email=author,
      url=url,
      packages=["aperture_contour"],
      install_requires=install_requires,
      zip_safe=False,
     )
