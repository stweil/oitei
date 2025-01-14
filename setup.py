from setuptools import setup

version = "2.0.0"

with open("README.md") as f:
    long_description = f.read()

setup(
    name="oitei",
    version=version,
    url="http://github.com/OpenITI/oitei",
    author="Raff Viglianti",
    author_email="rviglian@umd.edu",
    packages=["oitei", "oitei.corpus"],
    description="OpenITI mARkdown to TEI converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    test_suite="tests",
    python_requires=">=3.8.*",
    install_requires=[
        'lxml',
        'oimdp',
        'openiti'
    ],
)
