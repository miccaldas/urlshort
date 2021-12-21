from setuptools import setup

setup(
    name="urlshort",
    version=0.2,
    author="mclds",
    author_email="mclds@protonmail.com",
    description="URL shortener.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://codeberg.org/micaldas/urlshort",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["urlshort"],
    install_requires=[
        "urllib",
        "colr",
    ],
    include_package_data=True,
)
