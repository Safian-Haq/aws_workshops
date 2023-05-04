# AWS workshops web scrapping to excel

## Why I built this

Wanted a way to easily track my progress and select workshops I want to do for learning from [workshops.aws](workshops.aws).

### What does the script do

Run main.py to generate an xlsx file with details of each workshop from [workshops.aws](workshops.aws).

### Points of interest

-   Information only available when Javascript is loaded hence Selenium is used instead of HTML scrappers like BeautifulSoup.
-   Webdriver manager is used to always have the latest version of webdriver for Chrome. No more manual installs.
-   Pandas is used to convert data to excel.

### Future work

Create a website with the workshops table where people can mark their progress. Similar to [NeetCode](https://neetcode.io/practice).
