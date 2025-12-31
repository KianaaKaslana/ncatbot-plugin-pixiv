from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ncatbot-pixiv-plugin",
    version="1.0.0",
    author="shy_robot",
    author_email="",
    description="A Pixiv plugin for NcatBot that fetches and sends recommended images from Pixiv",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ncatbot-pixiv-plugin",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords=["ncatbot", "bot", "pixiv", "plugin"],
)