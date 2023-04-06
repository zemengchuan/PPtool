import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="PPtool",
    version='0.0.1',
    author="zemengchuan",
    author_email="zemengchuan@gmail.com",
    license="MIT",
    description=
    "PPtool is a Python third-party package that integrates many convenient methods for using the PPdata package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zemengchuan/PPtool",
    packages=setuptools.find_packages(),
    install_requires=[
        "fuzzywuzzy>=0.18.0",
        "pandas>=1.5"
    ],
    keywords=["PPshare", "webcrawler", "data", "PPdata", "tool"],
    package_data={"": ["*.py", "*.xlsx", "*.json", "*.pk", "*.js", "*.zip"]},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7")
