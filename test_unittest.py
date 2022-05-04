# unit tests

# import code to test
import committer
import unittest
import json

class Test_TestGithubOperations(unittest.TestCase):
    def setUp(self):
        # read credential file for access token
        f = open('local.credentials.json')
        d = json.load(f)
        self.access_token = d['access_token']
        f.close()

    def test_count_repos(self):
        self.assertEqual(committer.count_repos(self.access_token), 1)

if __name__ == '__main__':
    unittest.main()