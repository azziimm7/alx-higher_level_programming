#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
from sys import argv
import requests


if __name__ == "__main__":
    """ main """
    total = 0
    commit_str = "{}: {}"
    URL = "https://api.github.com/repos/{}/{}/commits"
    formated_url = URL.format(argv[2], argv[1])
    for commit in requests.get(formated_url).json():
        if total < 10:
            sha = commit.get("sha")
            name = commit.get("commit").get("author").get("name")
            print(commit_str.format(sha, name))
        total += 1
