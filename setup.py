from setuptools import setup


setup(
    name="python package example",
    version="0.0.1",
    description="test package usage",
    packages=[
        "jupyter_files"
    ],
    package_dir={
        "jupyter_files": "jupyter_files/"
    }
)