import json
import os

from Classi.Cliente import Cliente

class GestoreCliente:
    def __init__(self):
        self.listaClienti = []
        self.max_id = 0
        self.load_clienti()

    def load_clienti(self):
        if os.path.exists('Clienti.json'):
            try:
                with open('Clienti.json', 'r') as json_file:
                    data = json.load(json_file)
                    clienti_data = data.get("Clienti", [])
                    self.listaClienti = [
                        Cliente(
                            c["id"],
                            c["nome"],
                            c["cognome"],
                            c["codiceFiscale"],
                            c["dataDiNascita"],
                            c["email"],
                            c["luogoDiNascita"],
                            c["numeroDiTelefono"]
                        ) for c in clienti_data
                    ]
                    if self.listaClienti:
                        self.max_id = max(c.getId() for c in self.listaClienti)
            except Exception as e:
                print(f"Errore durante la lettura del file JSON: {str(e)}")

    def salva_clienti(self):
        try:
            with open('Clienti.json', 'w') as json_file:
                json.dump({"Clienti": [cliente.to_dict() for cliente in self.listaClienti]}, json_file, indent=4)
        except Exception as e:
            print(f"Errore durante la scrittura del file JSON: {str(e)}")

    def aggiungi_cliente(self, cliente):
        self.max_id += 1
        cliente.id = self.max_id
        self.listaClienti.append(cliente)
        self.salva_clienti()

    def rimuovi_cliente(self, cliente):
        for c in self.listaClienti:
            if c.id == cliente.id:
                self.listaClienti.remove(c)
                break

        self.salva_clienti()

    def modifica_cliente(self, cliente_aggiornato):
        for index, c in enumerate(self.listaClienti):
            if c.id == cliente_aggiornato.id:
                self.listaClienti[index] = cliente_aggiornato
                self.salva_clienti()
                return True

        return False