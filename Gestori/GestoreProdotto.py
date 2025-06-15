import json
import os
import random

from Classi.Film import Film
from Classi.Videogioco import Videogioco

class GestoreProdotto:
    def __init__(self):
        self.lista_prodotti = []
        self.load_prodotti()

    def load_prodotti(self):
        if os.path.exists('Prodotti.json'):
            try:
                with open('Prodotti.json', 'r') as json_file:
                    data = json.load(json_file)
                    prodotti_data = data.get("Prodotti", [])
                    self.lista_prodotti = []
                    for p in prodotti_data:
                        if p["tipo"] == "Film":
                            prodotto = Film(
                                p["id"], p["nome"], p["anno"], float(p["costoAcquisto"]),
                                float(p["costoNoleggio"]), p["disponibile"], p["unita"], p["tipo"],
                                p["dettagli"]["genereFilm"], p["dettagli"]["regista"]
                            )
                        elif p["tipo"] == "Videogioco":
                            prodotto = Videogioco(
                                p["id"], p["nome"], p["anno"], float(p["costoAcquisto"]),
                                float(p["costoNoleggio"]), p["disponibile"], p["unita"], p["tipo"],
                                p["dettagli"]["genereVideogioco"], p["dettagli"]["piattaforma"]
                            )
                        self.lista_prodotti.append(prodotto)
            except Exception as e:
                print(f"Errore durante la lettura del file JSON: {str(e)}")

    def salva_prodotti(self):
        try:
            with open('Prodotti.json', 'w') as json_file:
                json.dump({"Prodotti": [prodotto.to_dict() for prodotto in self.lista_prodotti]}, json_file, indent=4)
        except Exception as e:
            print(f"Errore durante la scrittura del file JSON: {str(e)}")

    def assegna_codice(self):
        while True:
            nuovo_id = random.randint(10000000, 99999999)
            if not any(p.id == nuovo_id for p in self.lista_prodotti):
                return nuovo_id

    def aggiungi_film(self, film):
        try:
            film.id = self.assegna_codice()
            self.lista_prodotti.append(film)
            self.salva_prodotti()
        except Exception as e:
            print(e)

    def aggiungi_videogioco(self, videogioco):
        videogioco.id = self.assegna_codice()
        self.lista_prodotti.append(videogioco)
        self.salva_prodotti()

    def rimuovi_prodotto(self, prodotto):
        self.lista_prodotti = [p for p in self.lista_prodotti if p.id != prodotto.id]
        self.salva_prodotti()

    def modifica_prodotto(self, prodotto_aggiornato):
        for index, p in enumerate(self.lista_prodotti):
            if p.id == prodotto_aggiornato.id:
                if prodotto_aggiornato.unita == 0:
                    prodotto_aggiornato.rendiNonDisponibile()
                else:
                    prodotto_aggiornato.rendiDisponibile()
                self.lista_prodotti[index] = prodotto_aggiornato
                self.salva_prodotti()
                return True

        return False