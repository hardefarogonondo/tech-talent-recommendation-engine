from setuptools import find_packages, setup

setup(
    name="ml_from_scratch",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
    author="Hardefa Rogonondo",
    author_email="hardefarogonondo@gmail.com",
    description="A matrix factorization library implemented from scratch",
    url='https://github.com/hardefarogonondo'
)
