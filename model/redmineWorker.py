from redmine import Redmine
from redmine.exceptions import AuthError, ResourceNotFoundError, ForbiddenError, ValidationError

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


    def getTaskData(self, taskNumber):
        try:
            task = self.api.issue.get(taskNumber)
            return [task.id, task.subject, task.project.name]
        except ResourceNotFoundError:
            return False
        except ForbiddenError:
            return False

    def setTime(self, taskId, date, hours, comment):
        try:
            response = self.api.time_entry.create(issue_id=taskId, spent_on=date, hours=hours, comments=comment)
            return response
        except ValidationError:
            return False

    def getProjects(self):
        projects = self.api.project.all()
        print(projects)
        return projects

    def getUrl(self):
        return self.url
