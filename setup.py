#!/usr/bin/env python

from setuptools import setup, find_packages

# https://packaging.python.org/guides/distributing-packages-using-setuptools/

if __name__ == "__main__":
    setup(
        name="selenium_with_python_and_docker",
        version="1.0.0",
        description="Selenium with Python",
        long_description="Selenium with Python using Docker",
        author="Wassim AZIRAR",
        packages=find_packages(exclude=["tests"], include=["scripts"]),
        license="MIT",
        install_requires=[],
        classifiers=[
            # 3=> Alpha, 4=> Beta, 5=> Production/Stable
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
        ],
    )
