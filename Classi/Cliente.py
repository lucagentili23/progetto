from Classi.Utente import Utente

class Cliente(Utente):

    def __init__(self, id, nome, cognome, codiceFiscale, dataDiNascita, email, luogoDiNascita, numeroDiTelefono):
        super().__init__(id, nome, cognome)
        self.codiceFiscale = codiceFiscale
        self.dataDiNascita = dataDiNascita
        self.email = email
        self.luogoDiNascita = luogoDiNascita
        self.numeroDiTelefono = numeroDiTelefono

    def getInfoCliente(self):
        return str(self.id) + "  -  " + self.getNomeCognome() + "  -  " + self.codiceFiscale

    def getCodiceFiscale(self):
        return self.codiceFiscale

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "codiceFiscale": self.codiceFiscale,
            "dataDiNascita": self.dataDiNascita,
            "email": self.email,
            "luogoDiNascita": self.luogoDiNascita,
            "numeroDiTelefono": self.numeroDiTelefono
        }