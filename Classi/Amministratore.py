from Classi.Utente import Utente

class Amministratore(Utente):

    def __init__(self, id, nome, cognome, username, password):
        super().__init__(id, nome, cognome)
        self.username = username
        self.password = password

    def getPassword(self):
        return self.password

    def getUsername(self):
        return self.username