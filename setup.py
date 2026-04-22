from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

version = "4.0.2"  

version_path = path.join(here, "telesignenterprise", "_version.py")
with open(version_path, "w") as f:
    f.write('"""Auto-generated version file"""\n__version__ = "{}"\n'.format(version))

try:
    with open(path.join(here, "README"), encoding="utf-8") as f:
        readme_content = f.read()
except (IOError, Exception):
    readme_content = ""

setup(
    name="telesignenterprise",
    version=version,
    description="Telesign Enterprise SDK",
    license="MIT License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    long_description=readme_content,
    keywords="telesign, sms, voice, mobile, authentication, identity, messaging",
    author="TeleSign Corp.",
    author_email="support@telesign.com",
    url="https://github.com/telesign/python_telesign",
    install_requires=["telesign >=4.0.0, <5.0.0"],
    packages=find_packages(exclude=["test", "test.*", "examples", "examples.*"]),
)