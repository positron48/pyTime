import configparser


class ConfigWorker:

    def __init__(self):
        self.configFilePath = 'settings.cfg'
        self.config = configparser.ConfigParser()
        self.config.read(self.configFilePath)

        self.redmines = self.getRedminesData()

    def save(self):
        with open(self.configFilePath, 'w') as configfile:
            self.config.write(configfile)

    def getRedminesData(self):
        redmines = []
        i = 1
        while "Redmine"+str(i) in self.config:
            i += 1
            redmines.append([
                self.config["Redmine" + str(i)]['url'],
                self.config["Redmine" + str(i)]['login'],
                self.config["Redmine" + str(i)]['token']
            ])
        return redmines

    def getEvolutionData(self):
        if "Evolution" in self.config:
            return [
                self.config["Evolution"]['url'],
                self.config["Evolution"]['login'],
                self.config["Evolution"]['token']
            ]
        return ["", "", ""]

    def setEvolution(self, data):
        self.config["Evolution"] = {}
        self.config["Evolution"]['url'] = data[0]
        self.config["Evolution"]['login'] = data[1]
        self.config["Evolution"]['token'] = ""
