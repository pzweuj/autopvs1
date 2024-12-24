from setuptools import setup, find_packages

setup(
    name="autopvs1",
    version="0.1.0",
    packages=find_packages(),
    package_data={"autopvs1": ["data/*", "config.ini"]},
    install_requires=[
        # 在这里列出依赖包
        "pyfaidx"
    ],
    author="pzweuj",
    author_email="pzweuj@live.com",  # 添加作者邮箱
    description="A tool for automatic PVS1 interpretation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pzweuj/autopvs1",  # 替换为实际的项目URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "autopvs1=autopvs1.autoPVS1:main",
        ],
    },
)

