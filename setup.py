from setuptools import setup, find_packages

setup(
    name="rate_limiter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    description="A Python package to handle rate limiting dynamically.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/rate-limiter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,  # Include non-Python files (e.g., config.json)
    package_data={
        "rate_limiter": ["config.json"],  # Include config.json in the package
    },
)