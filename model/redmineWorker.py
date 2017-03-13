from redmine import Redmine
from redmine.exceptions import AuthError

class RedmineWorker:

    def __init__(self, url):
        self.url = url

    def initWithLogin(self, login, password):
        self.api = Redmine(self.url, username=login, password=password)

    def initWithKey(self, key):
        self.api = Redmine(self.url, key=key)

    def getToken(self):
        try:
            user = self.api.user.get('current')
            return user.api_key
        except AuthError:
            return False