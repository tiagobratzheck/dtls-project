import random

class Client(object):

    def __init__(self, name):
        self.name = name


    def clientHello(self, server = ""):
        if server:
            return " Hello from " + self.name + " to " + server + " =>>>>>>", self.name
        else:
            return " Hello from " + self.name + "=>>>>>>", self.name


    def verifyCertificate(self, error):
        if error == 2:
            return " ALERT! BAD CERTIFICATE =>>>>>>"
        else:
            return " Ok! The " + self.name + " is gonna send the certificate! =>>>>>>"


    def sendCertificate(self):
        error = random.randint(1, 2)
        certificate = "This is a " + self.name + " certificate =>>>>>>"
        key = "This is a Key for the certificate =>>>>>>"
        return error, certificate, key
    

    def receiveCipherSpec(self, cipherSpec):
        if cipherSpec == 2:
            return " ALERT! DECRYPT ERROR =>>>>>>"
        else:
            return " Ok! The " + self.name + " and the Server can share application data by now =>>>>>>"             


    def finished(self):
        return " <<<<<<<= HANDSHAKE DTLS FINISHED =>>>>>>"




