from github import Github
import requests
import random
import os


body = ["Commit(s) made by you is/are not made using GITHUB CLI.", "Well, using GitHub Web for committing is a sin anyway, hence we decided to close your pull request. Try making another PR.", "Brehhh, we only accept commits using Github CLI", "Bleh bleh bleh!! Try again with Github CLI please.", "Desole, Nous sommes triste. Try making commits using GITHUB CLI"]

## export GPT="your_personal_token"
g = Github(os.environ["GPT"])

REPO_NAME = os.environ["REPO"]

repo = g.get_repo(REPO_NAME)

def pr_judge(number: int):
	pr = repo.get_pull(number)
	response = requests.get(url=f"https://api.github.com/repos/{REPO_NAME}/pulls/{number}/commits")
	if response.json()[-1]["committer"]["login"] == "web-flow":
			pr.create_issue_comment(body= random.choice(body))
			pr.edit(state = "closed")
	else:
		pr.create_issue_comment(body= "Your code will be reviewed soon. Make a new PR after your code is merged. Till then, Happy Coding !!")
