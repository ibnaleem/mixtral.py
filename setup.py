from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mixtral.py",
    version="0.0.1",
    author="Ibn Aleem",
    author_email="ibnaleem@outlook.com",
    description="A Python module for running the Mixtral-8x7B language model with customisable precision and attention mechanisms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ibnaleem/mixtral.py",
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=['torch', 'transformers']
)