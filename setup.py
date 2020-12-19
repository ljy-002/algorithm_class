import setuptools

with open("README.md", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="algorithm_class-gitignore",
    version="0.0.1",
    author="gitignore",
    author_email="ljy123ljy123@dingtalk.com",
    description="一个中文的算法库，欢迎大家使用！",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ljy-002/algorithm_class",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)