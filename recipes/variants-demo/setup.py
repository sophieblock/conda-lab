from setuptools import setup

setup(
    name="variants-demo",
    version="0.1.0",
    description="Demonstrates conda-build variants and build matrices",
    py_modules=["variants_demo"],
    entry_points={
        "console_scripts": [
            "variants-demo=variants_demo:main",
        ],
    },
    install_requires=[
        "numpy",
    ],
    python_requires=">=3.9",
)
