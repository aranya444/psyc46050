import setuptools

setuptools.setup(
    name="fibpackage",
    version="0.1.0",
    author="Aranya Adams",
    author_email="aranya@uchicago.edu",
    description="Coding tutorial for microscopy image analysis",
    url="https://github.com/aranya444/psyc46050,git",
    python_requires=">=3.9",
    packages=setuptools.find_packages(),
    install_requires=[
        'pathlib',
        'matplotlib',
        'numpy',
     'pandas',
    ],
)