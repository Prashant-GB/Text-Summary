import setuptools

with open("README.md", 'r', encoding="utf-8") as f:
    log_description = f.read()

__version__ = "0.0.0"

REPO_NAME= "TEXT-SUMMARIZATION"
AUTHOR_USER_NAME= "Prashant-GB"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL ="bhatprashantpg@gmail.com"


setuptools.setup(
    name= REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description="A small python nlp app",
    log_description=log_description,
    log_description_content = "rext/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    
    },
    package_dir={"":"src"},
    packages= setuptools.find_packages(where="src")

)

