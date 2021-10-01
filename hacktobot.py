from github import Github

g = Github("key_here")

repo = g.get_repo("MU-Enigma/Hacktoberfest_2020")

# print(dir(repo))
for commit in repo.get_commits():
	try:
		print(commit.committer.login)
	except Exception as e:
		print(f"Something went wrong bro: {e}")
		print(commit.raw_data["commit"]["committer"]["name"])