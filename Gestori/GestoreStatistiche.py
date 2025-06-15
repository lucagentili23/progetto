from Gestori.GestoreCliente import GestoreCliente
from Gestori.GestoreNoleggio import GestoreNoleggio
from Gestori.GestoreProdotto import GestoreProdotto
from Gestori.GestoreRicevuta import GestoreRicevuta

class GestoreStatistiche:
    def __init__(self):
        pass

    def storicoAcquisti(self):
        gestore_ricevute = GestoreRicevuta()
        ricevute = gestore_ricevute.listaRicevute

        ricevute.sort(key=lambda x: self.safe_int(x.dataEmissione))

        ricevute_filtrate = [r for r in ricevute if r.tipologia == "Acquisto"]

        ricevute_filtrate.sort(key=lambda x: self.safe_int(x.dataEmissione))

        return ricevute_filtrate

    def storicoNoleggi(self):
        gestore_noleggi = GestoreNoleggio()
        noleggi = gestore_noleggi.listaNoleggi

        noleggi.sort(key=lambda x: self.safe_int(x.dataInizio))

        gestore_prodotti = GestoreProdotto()
        gestore_clienti = GestoreCliente()
        prodotti = gestore_prodotti.lista_prodotti
        clienti = gestore_clienti.listaClienti

        gestore_ricevute = GestoreRicevuta()
        ricevute = gestore_ricevute.listaRicevute

        return noleggi, prodotti, clienti, ricevute

    def noleggiInCorso(self):
        gestore_noleggi = GestoreNoleggio()
        noleggi = gestore_noleggi.listaNoleggi
        noleggi.sort(key=lambda x: self.safe_int(x.dataInizio))

        noleggi.sort(key=lambda x: self.safe_int(x.dataInizio))

        gestore_prodotti = GestoreProdotto()
        gestore_clienti = GestoreCliente()
        prodotti = gestore_prodotti.lista_prodotti
        clienti = gestore_clienti.listaClienti

        righe = 0
        lista_noleggi_da_inserire = []

        for n in noleggi:
            if not n.restituito:
                lista_noleggi_da_inserire.append(n)
                righe += 1

        return noleggi, prodotti, clienti, righe, lista_noleggi_da_inserire

    def safe_int(self, val):
        try:
            return int(val)
        except (ValueError, TypeError):
            return float('inf')