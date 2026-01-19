from setuptools import setup

setup(
    name="hello-python",
    version="1.0.0",
    description="Simple Python package for conda recipe testing",
    py_modules=["hello_python"],
    entry_points={
        "console_scripts": [
            "hello-python=hello_python:main",
        ],
    },
    python_requires=">=3.10",
)
