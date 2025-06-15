from Classi.Prodotto import Prodotto

class Film(Prodotto):
    def __init__(self, id, nome, anno, costoAcquisto, costoNoleggio, disponibile, unita, tipo, genereFilm, regista):
        super().__init__(id, nome, anno, costoAcquisto, costoNoleggio, disponibile, unita, tipo)
        self.genereFilm = genereFilm
        self.regista = regista

    def getGenereFilm(self):
        return self.genereFilm

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["dettagli"] = {
            "genereFilm": self.genereFilm,
            "regista": self.regista
        }
        return base_dict