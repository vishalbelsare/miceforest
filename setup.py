from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8', errors='ignore') as fh:
    long_description = fh.read()


setup(
    name="miceforest",
    author="Samuel Wilson",
    license="MIT",
    author_email="samwilson303@gmail.com",
    test_suite="tests",
    description="Imputes missing data with MICE + random forests",
    keywords=['MICE','Imputation','Missing Values','Missing','Random Forest'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'lightgbm >= 3.3.1',
        'numpy',
        "blosc",
        "dill"
        ],
    extras_require={
        "Plotting": [
            'seaborn >= 0.11.0',
            'matplotlib >= 3.3.0'
        ],
        "Default_MM": [
            'scipy >= 1.6.0'
        ],
        "Testing": [
            "pandas",
            "sklearn"
        ],
    },
    url="https://github.com/AnotherSamWilson/miceforest",
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
