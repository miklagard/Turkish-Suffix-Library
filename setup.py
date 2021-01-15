import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="turkish-suffix-library",
    version="0.7.3",
    author="Cem Yildiz",
    author_email="cem.yildiz@ya.ru",
    description="Turkish suffix library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/miklagard/Turkish-Suffix-Library",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
