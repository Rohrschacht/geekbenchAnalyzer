#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

acknowledgement = """

Data provided by the Geekbench Browser
https://browser.geekbench.com/

Provided by
Primate Labs
1867 Yonge St. Suite 902
Toronto, Ontario, Canada
M4S 1Y5"""

if "-h" in sys.argv or "--help" in sys.argv:
    print(
        """Just give a search string for the Geekbench Browser.
The first result page will be fetched and averages and medians for single and multi core calculated.

Example:
$ ./geekbenchAnalyzer.py fx 8350
Single Score Average: 578.4
Multi Score Average: 2553.04
Single Score Median: 611
Multi Score Median: 2784"""
    )
    print(acknowledgement)
    sys.exit(0)


if len(sys.argv) <= 1:
    print("Need at least one argument for the Geekbench search!")
    sys.exit(1)

r = requests.get(
    "https://browser.geekbench.com/v5/cpu/search?q=" + "+".join(sys.argv[1:])
)

if r.status_code != 200:
    print("Something went wrong! Status Code: " + r.status_code)
    sys.exit(2)

soup = BeautifulSoup(r.text, "html.parser")

singleScores = []
multiScores = []

for div in soup.find_all("div", class_="col-6 col-md-3 col-lg-2"):
    if "Score" in div.span.text:
        if "Single" in div.span.text:
            scoreText = div.find_all("span")[1].text
            singleScores.append(int(scoreText))
        if "Multi" in div.span.text:
            scoreText = div.find_all("span")[1].text
            multiScores.append(int(scoreText))

print("Single Score Average: " + str(sum(singleScores) / len(singleScores)))
print("Multi Score Average: " + str(sum(multiScores) / len(multiScores)))

singleScores.sort()
multiScores.sort()

if len(singleScores) % 2 != 0:
    print("Single Score Median: " + str(singleScores[int(len(singleScores) / 2) + 1]))
else:
    print(
        "Single Score Median: "
        + str(
            (
                singleScores[len(singleScores) / 2]
                + singleScores[(len(singleScores) / 2) + 1]
            )
        )
    )

if len(multiScores) % 2 != 0:
    print("Multi Score Median: " + str(multiScores[int(len(multiScores) / 2) + 1]))
else:
    print(
        "Multi Score Median: "
        + str(
            (
                multiScores[len(multiScores) / 2]
                + multiScores[(len(multiScores) / 2) + 1]
            )
        )
    )

print(acknowledgement)
