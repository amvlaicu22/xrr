import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xrr-amvlaicu22", # Replace with your own username
    version="0.0.7",
    author="Vlaicu Aurel-Mihai",
    author_email="amvlaicu22@yahoo.com",
    description="X-ray reflectivity modeling for thin film multi-layer structures using Parrat algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amvlaicu22/xrr",
    packages=setuptools.find_packages(),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.ui", "*.wxg", "*.xrr", "*.dat", "*.sh"],
    },
    license="GNU General Public License v2 (GPLv2)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


