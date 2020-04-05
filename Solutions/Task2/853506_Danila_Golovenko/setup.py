import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="second_lab", # Replace with your own username
    version="1.0",
    author="Danila Golovenko",
    author_email="dgolovenko01@gmail.com",
    description="the full implementation of second lab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[]
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Linux",
    ],
    python_requires='>=3.6',
)