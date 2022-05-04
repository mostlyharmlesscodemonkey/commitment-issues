# main app

from github import Github


def count_repos(access_token=""):
    # using an access token
    g = Github(access_token)

    return g.get_user().get_repos().totalCount