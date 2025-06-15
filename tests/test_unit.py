import sys
from pathlib import Path
from unittest.mock import patch

# Rende importabili i moduli del progetto quando i test sono eseguiti
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from Classi.Prodotto import Prodotto
from Classi.Cliente import Cliente
from Gestori.GestoreCliente import GestoreCliente

# Verifica che "Prodotto.decrementa()" riduca "unita" di 1
def test_decrementa_unita():
    prodotto = Prodotto(
        id=1,
        nome="filmTest",
        anno=2002,
        costoAcquisto=10.0,
        costoNoleggio=2.5,
        disponibile=True,
        unita=5,
        tipo="Film",
    )

    prodotto.decrementa()

    assert prodotto.unita == 4
    # "disponibile" non deve cambiare (nel caso "unita" sia maggiore di 1)
    assert prodotto.disponibile is True

# Controlla le transizioni di disponibilità del prodotto
def test_gestione_disponibilita_prodotto():
    prodotto = Prodotto(
        id=2,
        nome="VideogiocoTest",
        anno=2002,
        costoAcquisto=10.0,
        costoNoleggio=2.5,
        disponibile=True,
        unita=1,
        tipo="Videogioco",
    )

    # Diventa non disponibile
    prodotto.rendiNonDisponibile()
    assert prodotto.unita == 0
    assert prodotto.disponibile is False

    # Torna disponibile
    prodotto.rendiDisponibile()
    assert prodotto.disponibile is True

# Verifica che "GestoreCliente.modifica_cliente()" aggiorni correttamente i dati.
def test_modifica_cliente():
    # Sostituisco per i test i metodi "load_clienti" e "salva_clienti" con funzioni "vuote"
    with patch.object(GestoreCliente, "load_clienti", lambda self: None), patch.object(
        GestoreCliente, "salva_clienti", lambda self: None
    ):
        gestore = GestoreCliente()
        gestore.listaClienti = []
        gestore.max_id = 0

        cliente_iniziale = Cliente(
            1,
            "Cliente1",
            "Test1",
            "ABCDEF0123456789",
            "2002-06-29",
            "cliente1@test.com",
            "cittaTest",
            "1234567890",
        )

        gestore.listaClienti.append(cliente_iniziale)

        # Cambio il cognome
        cliente_modificato = Cliente(
            1,
            "Cliente1",
            "Test2",
            "ABCDEF0123456789",
            "1980-06-29",
            "cliente1@test.com",
            "cittaTest",
            "1234567890",
        )

        risultato = gestore.modifica_cliente(cliente_modificato)

        assert risultato is True
        assert gestore.listaClienti[0].cognome == "Test2"
