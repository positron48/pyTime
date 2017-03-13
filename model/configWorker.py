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
        i = 0

        while "Redmine #"+str(i) in self.config:
            redmines.append([
                self.config["Redmine #" + str(i)]['url'],
                self.config["Redmine #" + str(i)]['login'],
                self.config["Redmine #" + str(i)]['token']
            ])
            i += 1

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
        self.config["Evolution"]['token'] = data[2]
        self.config["Evolution"]['employer_id'] = data[3]
        self.config["Evolution"]['employer_name'] = data[4]

    def saveRedmineData(self, data):
        for (i, item) in enumerate(data):
            self.config["Redmine #" + str(i)] = {}
            self.config["Redmine #" + str(i)]['url'] = item[0]
            self.config["Redmine #" + str(i)]['login'] = item[1]
            self.config["Redmine #" + str(i)]['token'] = item[2]
        self.save()
