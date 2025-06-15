from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QTableWidget, QHeaderView, \
    QTableWidgetItem, QMessageBox

from Gestori.GestoreMora import GestoreMora
from Gestori.GestoreNoleggio import GestoreNoleggio
from Gestori.GestoreStatistiche import GestoreStatistiche

class VistaNoleggiInCorso(QWidget):

    def __init__(self):
        try:
            super().__init__()

            self.setWindowTitle("VideoSpace")
            self.setFixedSize(1000, 600)

            font = QFont("impact", 20)

            layout = QVBoxLayout()

            label_titolo = QLabel("Noleggi in corso")
            label_titolo.setFont(font)
            layout.addWidget(label_titolo)

            self.tabella = QTableWidget()
            self.tabella.setColumnCount(9)
            self.tabella.setHorizontalHeaderLabels(
                ["Id prodotto", "Prodotto noleggiato", "Id noleggio", "Cognome cliente", "Id cliente", "Data inizio", "Data fine", "Mora addebitata", "Restituzione"])
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
            self.noleggi, self.prodotti, self.clienti, self.righe, self.lista_noleggi_da_inserire = gestore_statistiche.noleggiInCorso()

            self.popola_tabella(self.noleggi, self.prodotti, self.clienti, self.righe, self.lista_noleggi_da_inserire)

        except Exception as e:
            print(f"a:{e}")

    def popola_tabella(self, noleggi, prodotti, clienti, righe, lista_noleggi_da_inserire):
        try:
            self.tabella.setRowCount(righe)
            for row, noleggio in enumerate(lista_noleggi_da_inserire):
                if not noleggio.restituito:

                    nomeProdotto = "Non trovato"
                    for p in prodotti:
                        if p.id == noleggio.idProdotto:
                            nomeProdotto = p.nome
                            break

                    cognomeCliente = "Non trovato"
                    for c in clienti:
                        if c.id == noleggio.idCliente:
                            cognomeCliente = c.cognome
                            break

                    self.tabella.setItem(row, 0, QTableWidgetItem(str(noleggio.idProdotto)))
                    self.tabella.setItem(row, 1, QTableWidgetItem(str(nomeProdotto)))
                    self.tabella.setItem(row, 2, QTableWidgetItem(str(noleggio.id)))
                    self.tabella.setItem(row, 3, QTableWidgetItem(str(cognomeCliente)))
                    self.tabella.setItem(row, 4, QTableWidgetItem(str(noleggio.idCliente)))
                    self.tabella.setItem(row, 5, QTableWidgetItem(str(noleggio.dataInizio)))
                    self.tabella.setItem(row, 6, QTableWidgetItem(str(noleggio.dataFine)))

                    gestore_more = GestoreMora()

                    for m in gestore_more.listaMore:
                        if noleggio.id == m.idNoleggio:
                            self.tabella.setItem(row, 7, QTableWidgetItem(str(m.importo)))

                    bottone_restituisci = QPushButton("Restituisci")
                    bottone_restituisci.clicked.connect(self.on_click_restituisci)
                    self.tabella.setCellWidget(row, 8, bottone_restituisci)

            if not lista_noleggi_da_inserire:
                QMessageBox.information(self, 'Attenzione', 'Non sono presenti noleggi in corso', QMessageBox.Ok)
                self.close()
                return

            # Se la lista è vuota viene resettata la tabella
            if not noleggi:
                self.tabella.setRowCount(0)
        except Exception as e:
            print(f"b:{e}")

    def on_click_restituisci(self):
        try:
            gestore_noleggi = GestoreNoleggio()

            button = self.sender()  # Prende il pulsante che ha generato l'evento
            index = self.tabella.indexAt(button.pos())  # Prende l'indice della riga dalla posizione del pulsante
            row = index.row()  # Ricava la riga

            id_noleggio = int(self.tabella.item(row, 2).text())

            # Trova il noleggio corrispondente nella lista
            for noleggio in self.noleggi:
                if noleggio.id == id_noleggio:
                    noleggio.restituito = True
                    self.lista_noleggi_da_inserire.remove(noleggio)
                    break

            gestore_noleggi.modifica_noleggio(noleggio)

            # Rimuove la riga dalla tabella
            self.tabella.removeRow(row)

        except Exception as e:
            print(f"Errore durante la restituzione: {str(e)}")

    def on_click_indietro(self):
        from Viste.GestioneStatistiche.VistaStatistiche import VistaStatistiche
        self.vista_statisiche = VistaStatistiche()
        self.vista_statisiche.show()
        self.close()