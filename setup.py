import setuptools 

with open("README.md", "r") as f:
    long_description = f.read()

_version_ = "0.0.0"
Repo_NAME="chicken-disease-classification"   
AUTHOR_USERNAME="Fady-Atia"
SRC_REPO="chicken-disease-classification"
AUTHOR_EMAIL="fadyatia375@gmail.com"
setuptools.setup(
    name=Repo_NAME, 
    version=_version_,
    author=AUTHOR_USERNAME, 
    author_email=AUTHOR_EMAIL,
    description="A machine learning project for classifying chicken diseases using image data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Fady-Atia/chicken-disease-classification" , 
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{Repo_NAME}/issues",
    },
    # السطرين دول هما اللي هيحلوا الـ ModuleNotFoundError
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)  