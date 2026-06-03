from setuptools import setup, find_packages

setup(
    name="todo_manager",
    version="0.1.0",
    author="김승찬",
    description="Python 객체지향 기반 할 일 관리 패키지",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.0.0",
        "pycodestyle>=2.10.0"
    ],
)