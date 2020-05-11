from entities.client import Client
from entities.server import Server

import os, sys, time

class Service(object):

    def __init__(self):
        self.client = Client("Client")
        self.server = Server("Server")
    

    def cleaning(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def timing(self):
        time.sleep(2)
    

    def start(self):
        print("<<< ## BORA PRO FIGHT ## >>>\n")
        print("<<< Welcome! >>>\n")
        self.menu("1", "2", " - Run Fight 1 ", " - Exit \n", 1)
    

    def menu(self, a, b, text_a, text_b, fight):
        print("(" + a + ")" + text_a)
        print("(" + b + ")" + text_b)
        try:
            option = int(input("Select the option above: \n"))
            if option > 2:
                print("Invalid option...")
                return self.menu(a, b, text_a, text_b, fight)
            if option == 2:
                sys.exit()        
            else:                   
                return self.running(fight)                        
        except ValueError:
            print("Try one of the options above!")
            self.menu("1", "2", " - Run Fight 1 ", "- Exit \n", 1)

    
    def running(self, fight):
        if fight == 1:
            return self.runningFight1()
        if fight == 2:
            return self.runningFight2()
        if fight == 3:
            return self.runningFight3()
        if fight == 4:
            return self.runningFight4()

      
    def runningFight1(self):
        self.cleaning()
        print("\n <<< Starting the Fight 1: >>>\n")

        hello, client = self.client.clientHello()
        print(hello)
        self.timing()
        verify, serverName = self.server.verifyHello(client)
        print(verify)
        self.timing()
        secondHello, client = self.client.clientHello(serverName)
        print(secondHello)
        self.timing()
        serverHello = self.server.serverHello()
        print(serverHello)

        print("\n <<< End of Fight 1 >>>\n")
        self.menu("1", "2", " - Run Fight 2 ", " - Exit \n", 2)

    
    def runningFight2(self):        
        print("\n <<< Starting the Fight 2: >>>\n")

        error, certificate, key = self.server.sendCertificate()      
        alert = self.client.verifyCertificate(error)
        print(certificate)
        print(key)
        self.timing()
      
        while error != 1:
            print("\n" + alert)
            error, certificate, key = self.server.sendCertificate()
            print(certificate)
            print(key)
            alert = self.client.verifyCertificate(error)
            self.timing()
        
        print("\n " + alert)        
        print("\n <<< End of Fight 2 >>>\n")
        self.menu("1", "2", " - Run Fight 3 ", " - Exit \n", 3)
    

    def runningFight3(self):        
        print("\n <<< Starting the Fight 3: >>>\n")

        error, certificate, key = self.client.sendCertificate()      
        alert = self.server.verifyCertificate(error)
        print(certificate)
        print(key)
        self.timing()
      
        while error != 1:
            print("\n" + alert)
            error, certificate, key = self.client.sendCertificate()
            print(certificate)
            print(key)
            alert = self.server.verifyCertificate(error)
            self.timing()
        
        print("\n " + alert)        
        print("\n <<< End of Fight 3 >>>\n")
        self.menu("1", "2", " - Run Fight 4 ", " - Exit \n", 4)
    

    def runningFight4(self):
        print("\n <<< Starting the Fight 4: >>>\n")
        
        cipherSpec, cipherEncrypt = self.server.giveCipherSpec()
        alert = self.client.receiveCipherSpec(cipherEncrypt)
        print(cipherSpec)
        self.timing()

        while cipherEncrypt != 1:
            print("\n" + alert)
            cipherSpec, cipherEncrypt = self.server.giveCipherSpec()
            print(cipherSpec)
            alert = self.client.receiveCipherSpec(cipherEncrypt)
            self.timing()
        
        print("\n " + alert)        
        print("\n <<< End of Fight 4 >>>\n")

        print(self.client.finished())
            
        



