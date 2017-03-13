import requests

class EvoWorker:

    def __init__(self, url):
        self.url = url
        self.token = False

    def getToken(self, user, password):
        response = requests.post(self.url + "/api/auth", {"username":user, "password":password})
        response = response.json()

        if "success" in response and response['success'] == True:
            self.token = response['token']
            return self.token
        else:
            return False

