from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="Cerner-HealtheIntent",
    version="0.0.1",
    author="Patrick Gagnon",
    auther_email="plgagnon00@gmail.com",
    description="A wrapper following HealtheIntent open development services which allow access to population health concepts using RESTful APIs.",
    long_description=readme,
    url="https://github.com/patrickgagnon/Cerner-HealtheIntent",
    packages=['healtheintent-api'],
)
