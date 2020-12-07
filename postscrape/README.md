# Web Crawler

Simple web crawler created with Python to extract author name,date and title from the article( 'https://blog.scrapinghub.com/') and store in json file.


## Table of contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
- [Scope of functionalities](#Scope-of-functionalities)
- [The project status](#The-project-status)
- [Sources](#sources)



## General info

A Web crawler, sometimes called a spider or spiderbot and often shortened to crawler, is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing.



## Technologies

Project is created with:

- Python version: 3.6.9
- Scrapy Framework
- Html
- Css



## Setup


To run this project, install it locally using npm:

```
$ cd postscrape
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install scrapy
$ scrapy crawl posts
$ scrapy crawl -o posts.json

```


## Scope of functionalities

- This project for extracting the data you need from websites.
- In a fast, simple, yet extensible way.
- And data can be used various purposes like data mining,data analysis and information      processing.



## The project status

- The project is completed to extract the given information from the website.



## Sources

- Article by (https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/)
- Tutorial from the Traversey Media (https://www.youtube.com/watch?v=ALizgnSFTwQ)
- Documentation from the scrapy framework(https://scrapy.org/)
- Raw data from the ('https://blog.scrapinghub.com/')
