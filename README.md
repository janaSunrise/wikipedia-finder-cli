# Wikipedia Finder

This is a utility based Wikipedia Command line program, That helps you traverse the wikipedia, and Get data as you want, with features like searching, Suggestions, summaries and other stuff.

### Tech stack used

- `Requests`: Fetch all the data by scraping JSON Response from the API
- `Click`:  A python framework to build interactive CLI based programs
- `html2text`: A tool to remove redundant HTML.

### How to use it?

You can get it from pypi as a console package by using `pip install wikipedia-finder`

or if it doesn't work, you can install it manually by using these steps:

- Clone the repo
- `cd wikipedia-finder-cli`
- `python setup.py install`

### TODOs Planned

- [x] Cover `/feed/featured/{type}/{mm}/{dd}`
- [x] Cover `/page/html/{title}`
- [ ] Cover `/page/media-list/{title}`
- [ ] Cover `/page/segments/{title}`

Made by Sunrit Jana with ❤️
