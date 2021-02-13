import re
from pathlib import Path

import setuptools

# Files
BASE_DIR = Path(__file__).resolve().parent

README = Path(BASE_DIR / "README.md").read_text()

# Constants
VERSION = re.search(
    r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    Path(BASE_DIR / "wikifinder/__init__.py").read_text(),
    re.MULTILINE
).group(1)

URL = "https://github.com/janaSunrise/wikipedia-finder-cli"

if not VERSION:
    raise RuntimeError("VERSION is not set!")

# Setup
setuptools.setup(
    name="WikipediaFinderCLI",
    version=VERSION,

    author="Sunrit Jana",
    author_email="warriordefenderz@gmail.com",

    description="An interactive CLI version of traversing wikipedia and gaining knowledge!",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",

    url=URL,
    project_urls={
        "Documentation": URL,
        "Issue tracker": f"{URL}/issues",
    },

    packages=setuptools.find_packages(
        exclude=["tests", "tests.*", "tools", "tools.*"]
    ),
    entry_points={
        'console_scripts': [
            'wikifinder = wikifinder.__main__:wiki'
        ]
    },
    install_requires=[
        "requests==2.25.1",
        "click==7.1.2",
        "html2text==2020.1.16"
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

        "Programming Language :: Python :: Implementation :: CPython",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",

        "Natural Language :: English",
    ],

    python_requires='>=3.7',
)
