import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="frappeviz", # Replace with your own username
    version="0.0.0.1",
    author="Yemi Kudaisi",
    author_email="contact@yemikudaisi.online",
    description="Python app for visualizing class diagrams for a Frappe Framework App using PlantUML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yemikudaisi/frappe_viz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "plantuml==0.3.0",
    ]
)