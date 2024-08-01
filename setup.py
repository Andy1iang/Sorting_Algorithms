from setuptools import setup, find_packages

with open("description.md", "r") as fh:
    description = fh.read()

setup(
    name="SortVisualization",
    version=1.3,
    package=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "pygame",
    ],
    project_urls={
        "Repository": "https://github.com/Andy1iang/Sorting_Algorithms",
    },
    long_description=description,
    long_description_content_type="text/markdown",
)
