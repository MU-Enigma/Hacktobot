# Hacktobot
Bot to manage the PRs for Hacktoberfest

# Setup before running
- Clone this repository, and get a [GitHub access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- Setup [GitHub Webhook](https://docs.github.com/en/developers/webhooks-and-events/webhooks/about-webhooks) to send requests to your server.
- Add the repository to be monitored as the environment variable `REPO_NAME`. (On Linux, run `export REPO_NAME="<username>/<repository>)
- Similarly, export GitHub access token as `GPT` and webhook secrect as `GITHUB_SECRET`.

# Running
- launch a virtualenv if needed
- `pip install -r requirements.txt`
- Run it with any python WSGI server.