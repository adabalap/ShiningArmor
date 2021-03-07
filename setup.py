import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setuptools.setup(
    name="ShiningArmor", 
    version="0.0.2",
    author="Phani Adabala",
    author_email="adabala.phani@gmail.com",
    description="A collection of python functions for BOTs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adabalap/ShiningArmor",
    project_urls={
        "Bug Tracker": "https://github.com/adabalap/ShiningArmor/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
