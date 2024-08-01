from setuptools import setup, find_packages

setup(
    name = "SortVisualization",
    version = 1.2,
    package = find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires = [
        "pygame"
    ],
)