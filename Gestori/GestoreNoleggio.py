import json
import os

from Classi.Noleggio import Noleggio

class GestoreNoleggio:
    def __init__(self):
        self.listaNoleggi = []
        self.max_id = 0
        self.load_noleggi()

    def load_noleggi(self):
        if os.path.exists('Noleggi.json'):
            try:
                with open('Noleggi.json', 'r') as json_file:
                    data = json.load(json_file)
                    noleggi_data = data.get("Noleggi", [])
                    self.listaNoleggi = [
                        Noleggio(
                            n["id"],
                            n["dataInizio"],
                            n["dataFine"],
                            n["importo"],
                            n["idCliente"],
                            n["idProdotto"],
                            n["restituito"],
                        ) for n in noleggi_data
                    ]
                    if self.listaNoleggi:
                        self.max_id = max(n.getId() for n in self.listaNoleggi)
            except Exception as e:
                print(f"Errore durante la lettura del file JSON: {str(e)}")

    def salva_noleggi(self):
        try:
            with open('Noleggi.json', 'w') as json_file:
                json.dump({"Noleggi": [noleggio.to_dict() for noleggio in self.listaNoleggi]}, json_file, indent=4)
        except Exception as e:
            print(f"Errore durante la scrittura del file JSON: {str(e)}")

    def aggiungi_noleggio(self, noleggio):
        self.max_id += 1
        noleggio.id = self.max_id
        self.listaNoleggi.append(noleggio)
        self.salva_noleggi()

    def modifica_noleggio(self, noleggio_aggiornato):
        for index, n in enumerate(self.listaNoleggi):
            if n.id == noleggio_aggiornato.id:
                self.listaNoleggi[index] = noleggio_aggiornato
                self.salva_noleggi()
                return True

        return False