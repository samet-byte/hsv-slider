from setuptools import setup, find_packages

setup(
    name="hsv-slider",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "opencv-python",
        "numpy",
    ],
    author="Sam",
    author_email="bayatsamet13@gmail.com",
    description="A module for creating HSV color sliders using OpenCV",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/samet-byte/hsv-slider",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
