from setuptools import setup, find_packages

with open('requirements.txt', 'r') as _f:
    requirements = [line for line in _f.read().split('\n') ]

setup(
    name="summarize",
    version="0.0.1",
    description="CLI tool to summarize text using huggingface",
    install_requires = requirements,
    entry_points="""
    [console_scripts]
    summarize= huggingface.summarize:main        
    """,
    author="Subek Acharya",
    author_email="subekacharya@uri.edu",
    packages=find_packages(),
)

