class Utente:

    def __init__(self, id, nome, cognome):
        self.id = id
        self.nome = nome
        self.cognome = cognome

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getNomeCognome(self):
        return self.nome + " " + self.cognome