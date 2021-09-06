import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setuptools.setup(
    name="ShiningArmor", 
    version="1.0.0",
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
    install_requires=[
        "certifi==2021.5.30",
        "charset-normalizer==2.0.4",
        "EasyProcess==0.3",
        "idna==3.2",
        "oauthlib==3.1.1",
        "PySocks==1.7.1",
        "PyVirtualDisplay==2.2",
        "requests==2.26.0",
        "requests-oauthlib==1.3.0",
        "selenium==3.141.0",
        "six==1.16.0",
        "tweepy==3.10.0",
        "urllib3==1.26.6"
    ]
)
