class Noleggio:

    def __init__(self, id, dataInizio, dataFine, importo, idCliente, idProdotto, restituito):
        self.id = id
        self.dataInizio = dataInizio
        self.dataFine = dataFine
        self.importo = importo
        self.idCliente = idCliente
        self.idProdotto = idProdotto
        self.restituito = restituito

    def to_dict(self):
        return {
            "id": self.id,
            "dataInizio": self.dataInizio,
            "dataFine": self.dataFine,
            "importo": self.importo,
            "idCliente": self.idCliente,
            "idProdotto": self.idProdotto,
            "restituito": self.restituito
        }

    def getId(self):
        return self.id

    def getDataInizio(self):
        return self.dataInizio

    def getDataFine(self):
        return self.dataFine