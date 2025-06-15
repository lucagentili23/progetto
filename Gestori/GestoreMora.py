import json
import os

from Classi.Mora import Mora

class GestoreMora:
    def __init__(self):
        self.listaMore = []
        self.max_id = 0
        self.load_more()

    def load_more(self):
        if os.path.exists('More.json'):
            try:
                with open('More.json', 'r') as json_file:
                    data = json.load(json_file)
                    more_data = data.get("More", [])
                    self.listaMore = [
                        Mora(
                            m["id"],
                            m["dataEmissioneUltima"],
                            m["importo"],
                            m["idNoleggio"]
                        ) for m in more_data
                    ]
                    if self.listaMore:
                        self.max_id = max(m.getId() for m in self.listaMore)
            except Exception as e:
                print(f"Errore durante la lettura del file JSON more: {str(e)}")

    def salva_mora(self):
        try:
            with open('More.json', 'w') as json_file:
                json.dump({"More": [mora.to_dict() for mora in self.listaMore]}, json_file, indent=4)
        except Exception as e:
            print(f"Errore durante la scrittura del file JSON: {str(e)}")

    def aggiungi_mora(self, mora):
        self.max_id += 1
        mora.id = self.max_id
        self.listaMore.append(mora)
        self.salva_mora()

    def modifica_mora(self, mora_aggiornata):
        for index, m in enumerate(self.listaMore):
            if m.id == mora_aggiornata.id:
                self.listaMore[index] = mora_aggiornata
                self.salva_mora()
                return True
        return False