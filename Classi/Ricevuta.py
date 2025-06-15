class Ricevuta:

    def __init__(self, id, cliente, dataEmissione, importo, prodotto, tipologia, idTipologia):
        self.id = id
        self.cliente = cliente
        self.dataEmissione = dataEmissione
        self.importo = importo
        self.prodotto = prodotto
        self.tipologia = tipologia
        self.idTipologia = idTipologia

    def to_dict(self):
        return {
            'id': self.id,
            'cliente': self.cliente.to_dict() if self.cliente else None,
            'dataEmissione': self.dataEmissione,
            'importo': self.importo,
            'prodotto': self.prodotto.to_dict() if self.prodotto else None,
            'tipologia': self.tipologia,
            "idTipologia": self.idTipologia
        }

    def getId(self):
        return self.id