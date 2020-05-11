import random

class Server(object):
    
    def __init__(self, name):
        self.name = name


    def verifyHello(self, hello):
        return "<<<<<<= Verify the " + hello + " hello... ", self.name


    def serverHello(self):
        return "<<<<<<= Hello from " + self.name + " ."    


    def sendCertificate(self):
        error = random.randint(1, 2)
        certificate = "<<<<<<= This is the " + self.name + " certificate"
        key = "<<<<<<= This is a Key for the " + self.name + " certificate"
        return error, certificate, key    


    def verifyCertificate(self, error):
        if error == 2:
            return "<<<<<<= ALERT! BAD CERTIFICATE "
        else:
            return "<<<<<<= OK! It looks like everything is fine! We gonna send the chiper spec. "    
    
    
    def giveCipherSpec(self):
        cipherSpec = "<<<<<<= This is the encrypted server specification for the Client "
        cipherEncrypt = random.randint(1, 2)
        return cipherSpec, cipherEncrypt
    