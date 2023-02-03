from setuptools import setup, find_packages

setup(
    name="html5tagger",
    author="Sanic Community",
    author_email="tronic@noreply.users.github.com",
    description="Pythonic HTML generation/templating (no template files)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sanic-org/html5tagger",
    packages=find_packages(),
    keywords=["HTML", "HTML5", "templating", "Jinja2"],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Text Processing :: Markup :: HTML",
        "License :: OSI Approved :: MIT License",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.7",
    use_scm_version=True,
    setup_requires = ["setuptools_scm"],
    install_requires = [],
    include_package_data = True,
)
