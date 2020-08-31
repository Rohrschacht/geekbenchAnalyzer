# geekbenchAnalyzer.py

## About

geekbenchAnalyzer.py is an analyzer for data provided by the [Geekbench
Browser](https://browser.geekbench.com). It takes a search query from you and
requests the first result page from Geekbench as if you had typed it in there
yourself. This result page is then scanned for the single- and multi-core
scores. The average and median of these results is then presented to you -- no
need typing all of that into your calculator anymore.

## Example

```
$ ./geekbenchAnalyzer.py fx 8350
Single Score Average: 578.4
Multi Score Average: 2553.04
Single Score Median: 611
Multi Score Median: 2784


Data provided by the Geekbench Browser
https://browser.geekbench.com/

Provided by
Primate Labs
1867 Yonge St. Suite 902
Toronto, Ontario, Canada
M4S 1Y5
```

## Installation

Make sure you have current versions of
[Python 3](https://www.python.org/downloads/) and pip installed (pip usually
comes with Python 3). Install the required components with:

```
$ pip install -r requirements.txt
```

## Acknowledgements

This program fetches data from the [Geekbench
Browser](https://browser.geekbench.com) to calculate the statistics. [Geekbench
5](https://www.geekbench.com/) is a cross-platform system's performance
benchmark. You should check it out.

Geekbench and the Geekbench Browser are copyright of:  
Primate Labs  
1867 Yonge St. Suite 902  
Toronto, Ontario, Canada  
M4S 1Y5

This tool makes use of the following awesome open source projects:

- [Python 3](https://www.python.org/)
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/)
