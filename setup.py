from pathlib import Path

from setuptools import find_packages, setup


BASE_DIR = Path(__file__).parent
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")
REQUIREMENTS = [
    line.strip()
    for line in (BASE_DIR / "requirements.txt").read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.startswith("#")
]


setup(
    name="image-processing-vinicius",
    version="0.1.0",
    author="Vinicius Melo",
    author_email="viniciusdmelogomes@gmail.com",
    description="Pacote simples para processamento de imagens desenvolvido no curso da DIO.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/viniciusmelo7/image-processing-package-vinicius",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
