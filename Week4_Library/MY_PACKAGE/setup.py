from setuptools import setup, find_packages

setup(
    name="test_saying",          # 包名称（pip安装时用）
    version="0.1.0",            # 版本号
    packages=find_packages(),   # 自动包含所有包
    author="Yizhao Wang",
    description="A simple example package",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
)