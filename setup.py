from setuptools import setup, find_packages

setup(
    name="devhelper-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="DevHelper CLI - Automate development tasks efficiently.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/DevHelper-CLI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "devhelper=devhelper.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
