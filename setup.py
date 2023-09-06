import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"
REPO_NAME ="Text-Summarizer"
AUTHOR_USER_NAME = "prashantuchiha"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="dahiya.prashant210@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prashantuchiha/Text-Summarizer",
    project_urls={
        "Bug Tracker": "https://github.com/prashantuchiha/Text-Summarizer/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)