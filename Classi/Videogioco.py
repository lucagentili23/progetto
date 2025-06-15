from Classi.Prodotto import Prodotto

class Videogioco(Prodotto):

    def __init__(self, id, nome, anno, costoAcquisto, costoNoleggio, disponibile, unita, tipo, genereVideogioco, piattaforma):
        super().__init__(id, nome, anno, costoAcquisto, costoNoleggio, disponibile, unita, tipo)
        self.genereVideogioco = genereVideogioco
        self.piattaforma = piattaforma

    def getGenereVideogioco(self):
        return self.genereVideogioco

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["dettagli"] = {
            "genereVideogioco": self.genereVideogioco,
            "piattaforma": self.piattaforma
        }
        return base_dict