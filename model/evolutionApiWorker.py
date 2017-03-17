import requests
import datetime

class EvoWorker:

    def __init__(self, url, token=False):
        self.url = url
        self.token = token

    def getToken(self, user, password):
        response = requests.post(self.url + "/api/auth", {"username":user, "password":password})
        response = response.json()

        if "success" in response and response['success'] == True:
            self.token = response['token']
            return self.token
        else:
            return False

    def getEmployeers(self, name=False):
        params = {"token":self.token}
        if name != False:
            params['title_start'] = name

        response = requests.get(self.url + "/api/employee", params)
        response = response.json()

        if "data" in response and len(response['data']) > 0:
            return response['data']
        else:
            return False

    def getEmployeerId(self, name=False):
        employeers = self.getEmployeers(name)
        if len(employeers) == 1:
            return employeers[0]['id']
        return False

    def getProjects(self, name=False):
        params = {"token":self.token}
        if name != False:
            params['title_start'] = name

        response = requests.get(self.url + "/api/project", params)
        response = response.json()

        if "data" in response and len(response['data']) > 0:
            return response['data']
        else:
            return False

    def sendTask(self, name, date, hours, comment, employerId, projectId):
        if len(date) == 8:
            date = datetime.datetime.strptime(date, "%d.%m.%y").date().strftime('%d.%m.%Y')


        params = {
            "token": self.token,
            "name": name,
            "date": date,
            "hours": hours,
            "comment": comment,
            "employee_id": employerId,
            "project_id": projectId
        }

        response = requests.post(self.url + "/api/task", params)

        response = response.json()

        if "success" in response and response['id'] > 0:
            return response['id']
        else:
            return response['id']