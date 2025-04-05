from setuptools import setup, find_packages

setup(
    name="macpy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pyobjc-core>=9.2',
        'pyobjc-framework-Cocoa>=9.2',
    ],
    author="Meet Sonawane",
    author_email="meetsonawane1715@gmail.com",
    description="A Python framework for creating native macOS applications",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/macpy",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7',
)