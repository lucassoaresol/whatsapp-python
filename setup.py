from setuptools import find_packages, setup

setup(
    name="whatsapp",
    version="0.1.0",
    description="Python client for Whatsapp API",
    author="Lucas Soares",
    author_email="lucassoaresolv@outlook.com",
    url="https://github.com/lucassoaresol/whatsapp-python",
    packages=find_packages(),
    install_requires=[
        "python-dotenv>=1.1.0",
        "requests>=2.32.3",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
