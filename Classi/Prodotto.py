class Prodotto:

    def __init__(self, id, nome, anno, costoAcquisto, costoNoleggio, disponibile, unita, tipo):
        self.id = id
        self.nome = nome
        self.anno = anno
        self.costoAcquisto = costoAcquisto
        self.costoNoleggio = costoNoleggio
        self.disponibile = disponibile
        self.unita = unita
        self.tipo = tipo

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getAnno(self):
        return self.anno

    def getCostoAcquisto(self):
        return self.costoAcquisto

    def getCostoNoleggio(self):
        return self.costoNoleggio

    def getTipo(self):
        return self.tipo

    def decrementa(self):
        self.unita -= 1

    def rendiNonDisponibile(self):
        self.unita = 0
        self.disponibile = False

    def rendiDisponibile(self):
        self.disponibile = True

    def to_dict(self):
        return {
            "id": self.id,
            "anno": self.anno,
            "costoAcquisto": self.costoAcquisto,
            "costoNoleggio": self.costoNoleggio,
            "disponibile": self.disponibile,
            "nome": self.nome,
            "unita": self.unita,
            "tipo": self.__class__.__name__
        }