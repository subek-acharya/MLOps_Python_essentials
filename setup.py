from setuptools import setup, find_packages

setup(
    name="jformat",
    version="0.0.1",
    description="Reformats files to stdout",
    install_requires = ["click", "colorama"],
    entry_points="""
    [console_scripts]
    jformat= custom_cli.jformat:main
    """,
    author="Subek Acharya",
    author_email="subekacharya@uri.edu",
    packages=find_packages(),
)

