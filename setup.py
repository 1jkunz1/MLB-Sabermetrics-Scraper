# -*- coding: utf-8 -*-

setup(
    name="MLB Scarper",
    description="Fangraphs MLB Scraper",
    long_description="Fangraphs MLB Scraper",
    author="Joseph Kunzler",
    author_email="josephrkunzler@gmail.com",
    url="https://www.haloshark.com",
    download_url=repo,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python", ],
    include_package_data=True,
    package_data={'': ['.boto', '*.ico', '*.yaml', '*.wav', '*.html', '*.png',
                       '*.jpg', '*.css', '*.js', '*.map', '*.svg', '*.ttf',
                       '*.eot', '*.woff', '*.woff2'],
                  },
    entry_points={

    },
    data_files=[
    ],
    dependency_links=[
    ],
)
