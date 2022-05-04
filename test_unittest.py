# unit tests

# TODO: need to create some way to inject the client through an interface because these
# all make network calls to the real api so aren't really unit tests.

# import code to test
from committer import Committer
import unittest
import json

class Test_TestGithubOperations(unittest.TestCase):
    def setUp(self):
        # read credential file for access token
        f = open('local.credentials.json')
        d = json.load(f)
        f.close()
        self.app = Committer(d['access_token'])
        self.repo_name = d['repo_name']

    def test_count_repos(self):
        self.assertEqual(self.app.count_repos(), 1)

    def test_has_master_branch_positive(self):
        self.assertEqual(self.app.has_master_branch(self.repo_name), True)

    def test_has_master_branch_negative(self):
        self.assertEqual(self.app.has_master_branch('non-existent-repo'), False)
    
    def test_generate_filename_unique(self):
        gen_1 = self.app.generate_filename('prefix')
        gen_2 = self.app.generate_filename('prefix')
        self.assertNotEqual(gen_1, gen_2)

    def test_commit_add_file(self):
        file_name = self.app.generate_filename('prefix')
        self.assertIsNotNone(self.app.commit_add_file(self.repo_name, "test", "test: added a new file", file_name=file_name, data="wowee"))
    
    # delete file on branch

    # merge open PR automagically?


if __name__ == '__main__':
    unittest.main()