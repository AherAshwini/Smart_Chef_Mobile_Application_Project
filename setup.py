from setup import setup, find_packages

setup(
    name="Smart Chef Mobile Application",
    version="0.1.0",
    author="Ashwini Aher",
    author_email="aherashwini25@gmail.com",
    packages=find_packages(),
    install_requires=["numpy", "pandas", "seaborn", "scikit-learn", "flask", "sqlalchemy", "pytest", "flake8"]
    
)