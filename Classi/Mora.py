class Mora:

    def __init__(self, id, dataEmissioneUltima, importo, idNoleggio):
        self.id = id
        self.dataEmissioneUltima = dataEmissioneUltima
        self.importo = importo
        self.idNoleggio = idNoleggio

    def to_dict(self):
        return {
            "id": self.id,
            "dataEmissioneUltima": self.dataEmissioneUltima,
            "importo": self.importo,
            "idNoleggio": self.idNoleggio
        }

    def getId(self):
        return self.id