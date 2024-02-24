from setuptools import setup, find_packages

setup(
    name='javScrapy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scrapy',
        'pandas',
        'selenium',
    ],
    entry_points={
        'scrapy': [
            'settings = javScrapy.settings'
        ],
    },
    # Metadata
    author='mrbruce516',
    author_email='mrbruce516@gmail.com',
    description='获取当日javbus高清磁力链',
    url='https://github.com/mrbruce516/scrapy',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
