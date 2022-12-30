from setuptools import setup

# Read the contents of the README.md file
with open("README.md", "r") as f:
    long_description = f.read()

name = 'mlskeleton'
version = "0.0.1-dev0"
description = 'A Python package that generates a folder structure for machine learning/deep learning projects'
author = 'Sathiyakugan B'
author_email = 'sathiyakugan.bala@gmail.com'
homepage = 'https://github.com/Sathiyakugan/mlskeleton#README'
bug_tracker = 'https://github.com/asgardeo/mlskeleton/issues'
download_url = 'https://github.com/asgardeo/mlskeleton/releases'
keywords = [
    "machinelearning",
    "deeplearning",
    "OIDC",
    "folderskeleton",
    "bootstraptemplate",
    "projecttemplate"
]

setup(name=name,
      version=version,
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url=homepage,
      download_url=download_url,
      author=author,
      include_package_data=True,
      keywords=keywords,
      author_email=author_email,
      license='MIT',
      packages=['mlskeleton'],
      package_data={"mlskeleton": ["folder_structure.json"]},
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      entry_points={
          'console_scripts': ['mlskeleton=mlskeleton.generator:main'],
      },
      zip_safe=False,
      project_urls={
          'Documentation': homepage,
          'Bug Tracker': bug_tracker,
          'Source Code': homepage,
      }
      )
