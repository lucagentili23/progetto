import json
import os

from Classi.Cliente import Cliente
from Classi.Prodotto import Prodotto
from Classi.Ricevuta import Ricevuta


class GestoreRicevuta:
    def __init__(self):
        self.listaRicevute = []
        self.max_id = 0
        self.load_ricevute()

    def load_ricevute(self):
        if os.path.exists('Ricevute.json'):
            try:
                with open('Ricevute.json', 'r') as json_file:
                    data = json.load(json_file)
                    ricevute_data = data.get("Ricevute", [])
                    self.listaRicevute = []
                    for r in ricevute_data:
                        cliente = Cliente(
                            r["cliente"]["id"],
                            r["cliente"]["nome"],
                            r["cliente"]["cognome"],
                            r["cliente"]["codiceFiscale"],
                            r["cliente"]["dataDiNascita"],
                            r["cliente"]["email"],
                            r["cliente"]["luogoDiNascita"],
                            r["cliente"]["numeroDiTelefono"]
                        )
                        prodotto = Prodotto(
                            r["prodotto"]["id"],
                            r["prodotto"]["nome"],
                            r["prodotto"]["anno"],
                            r["prodotto"]["costoAcquisto"],
                            r["prodotto"]["costoNoleggio"],
                            r["prodotto"]["disponibile"],
                            r["prodotto"]["unita"],
                            r["prodotto"]["tipo"]
                        )
                        self.listaRicevute.append(Ricevuta(
                            r["id"], cliente, r["dataEmissione"],
                            r["importo"], prodotto, r["tipologia"], r["idTipologia"]
                        ))
                    if self.listaRicevute:
                        self.max_id = max(r.getId() for r in self.listaRicevute)
            except Exception as e:
                print(f"Errore durante la lettura del file JSON: {str(e)}")

    def salva_ricevute(self):
        try:
            with open('Ricevute.json', 'w') as json_file:
                json.dump({"Ricevute": [ricevuta.to_dict() for ricevuta in self.listaRicevute]}, json_file, indent=4)
        except Exception as e:
            print(f"Errore durante la scrittura del file JSON: {str(e)}")

    def aggiungi_ricevuta(self, ricevuta):
        self.max_id += 1
        ricevuta.id = self.max_id
        self.listaRicevute.append(ricevuta)
        self.salva_ricevute()