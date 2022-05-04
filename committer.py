# main app

from github import Github
import uuid

class Committer:

    def __init__(self, access_token=""):
        '''Set up the main app class'''
        self._access_token = access_token
        self.client = Github(access_token)

    def count_repos(self):
        '''Returns the count of repositories on the user\'s github account'''
        return self.client.get_user().get_repos().totalCount

    def has_master_branch(self, repo_name=""):
        '''Returns True when there\'s a master branch on the repository; False otherwise'''
        try:
            user = self.client.get_user()
            repo = user.get_repo(repo_name)
            branch = repo.get_branch(branch="master")
            print(branch.name)
        except:
            return False
        return True
    
    def commit_add_file(self, repo_name="", branch_name="master", commit_msg="Added new file", file_name="new_file.txt", data=""):
        '''Commits a new file to the given repository'''
        user = self.client.get_user()
        repo = user.get_repo(repo_name)
        created = repo.create_file(file_name, commit_msg, data, branch_name)
        return created
    
    def generate_filename(self, prefix):
        '''Returns unique filename based on the given prefix'''
        separator = "_"
        extension = "txt"
        file_name = ".".join([separator.join([prefix, str(uuid.uuid4())]), extension])
        return file_name