from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QTableWidget, QHeaderView, \
    QTableWidgetItem, QMessageBox

from Gestori.GestoreStatistiche import GestoreStatistiche

class VistaStoricoNoleggi(QWidget):

    def __init__(self):
        try:
            super().__init__()

            self.setWindowTitle("VideoSpace")
            self.setFixedSize(1000, 600)

            font = QFont("impact", 20)

            layout = QVBoxLayout()

            label_titolo = QLabel("Storico noleggi")
            label_titolo.setFont(font)
            layout.addWidget(label_titolo)

            self.tabella = QTableWidget()
            self.tabella.setColumnCount(8)
            self.tabella.setHorizontalHeaderLabels(
                ["Id ricevuta", "Prodotto noleggiato", "Nome cliente", "Cognome cliente", "Id cliente", "Data inizio", "Data fine", "Importo"])
            self.tabella.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tabella.verticalHeader().setVisible(False)

            layout.addWidget(self.tabella)

            layout.addSpacing(20)

            hbox = QHBoxLayout()
            hbox.addStretch(1)
            pulsante_indietro = QPushButton("Indietro")
            pulsante_indietro.setFixedWidth(150)
            hbox.addWidget(pulsante_indietro)
            hbox.addStretch(1)
            layout.addLayout(hbox)

            pulsante_indietro.clicked.connect(self.on_click_indietro)

            self.setLayout(layout)

            gestore_statistiche = GestoreStatistiche()
            noleggi, prodotti, clienti, ricevute = gestore_statistiche.storicoNoleggi()

            self.popola_tabella(noleggi, prodotti, clienti, ricevute)
        except Exception as e:
            print(f"Errore nell'inizializzazione: {e}")

    def popola_tabella(self, noleggi, prodotti, clienti, ricevute):
        try:
            self.tabella.setRowCount(len(noleggi))
            for row, noleggio in enumerate(noleggi):
                for r in ricevute:
                    if r.tipologia == "Noleggio" and noleggio.getId() == r.idTipologia:
                        self.tabella.setItem(row, 0, QTableWidgetItem(str(r.getId())))

                # Trova il prodotto associato al noleggio
                nomeProdotto = "Non trovato"
                for p in prodotti:
                    if p.getId() == noleggio.idProdotto:
                        nomeProdotto = p.nome
                        break
                self.tabella.setItem(row, 1, QTableWidgetItem(str(nomeProdotto)))

                # Trova il cliente associato al noleggio
                nomeCliente = "Non trovato"
                cognomeCliente = "Non trovato"
                for c in clienti:
                    if c.getId() == noleggio.idCliente:
                        nomeCliente = c.nome
                        cognomeCliente = c.cognome
                        break
                self.tabella.setItem(row, 2, QTableWidgetItem(str(nomeCliente)))
                self.tabella.setItem(row, 3, QTableWidgetItem(str(cognomeCliente)))
                self.tabella.setItem(row, 4, QTableWidgetItem(str(noleggio.idCliente)))
                self.tabella.setItem(row, 5, QTableWidgetItem(str(noleggio.dataInizio)))
                self.tabella.setItem(row, 6, QTableWidgetItem(str(noleggio.dataFine)))
                self.tabella.setItem(row, 7, QTableWidgetItem(str(noleggio.importo)))

            # Se la lista è vuota viene resettata la tabella
            if not noleggi:
                self.tabella.setRowCount(0)
                QMessageBox.information(self, 'Attenzione', 'Non sono ancora stati registrati noleggi', QMessageBox.Ok)
                self.close()
                return
        except Exception as e:
            print(f"Errore durante il filtraggio dei noleggi: {e}")

    def on_click_indietro(self):
        from Viste.GestioneStatistiche.VistaStatistiche import VistaStatistiche
        self.vista_statistiche = VistaStatistiche()
        self.vista_statistiche.show()
        self.close()