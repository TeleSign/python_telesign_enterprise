from setuptools import setup, find_packages

version = "2.1.5"

try:
    with open("README") as f:
        readme_content = f.read()
except (IOError, Exception):
    readme_content = ""

setup(name='telesignenterprise',
      version=version,
      description="Telesign Enterprise SDK",
      license="MIT License",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English"
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
      ],
      long_description=readme_content,
      keywords='telesign, sms, voice, mobile, authentication, identity, messaging',
      author='TeleSign Corp.',
      author_email='support@telesign.com',
      url="https://github.com/telesign/python_telesign",
      install_requires=['telesign >=2.2.1, <2.3'],
      packages=find_packages(exclude=['test', 'test.*', 'examples', 'examples.*']),
      )
