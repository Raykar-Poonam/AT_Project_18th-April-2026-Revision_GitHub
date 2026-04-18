import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\Configuration\\config.ini")

class Readconfig:

    @staticmethod
    def getUsername():
        Username = config.get("login data","username")
        return Username

    @staticmethod
    def getPasssword():
        Password = config.get("login data","password")
        return Password
