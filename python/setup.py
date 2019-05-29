import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dice_tower",
    version="1.2.13",
    author="Ian Hunter",
    author_email="hunterif@tcd.ie",
    description="Dice Rolling Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ianfhunter/dice-tower",
    packages=setuptools.find_packages(),
    install_requires=[
        'antlr4-python3-runtime>=4.7.2'
    ],
    package_data={
        'dice_tower.links': ['*.dice'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
