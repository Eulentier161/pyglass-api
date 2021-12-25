from setuptools import setup, find_packages

setup(
    name="pyglass-api",
    version="0.1.1",
    packages=find_packages(include=["pyglass", "pyglass.*"]),
    install_requires=["requests", "certifi", "charset-normalizer", "idna", "urllib3"],
)
