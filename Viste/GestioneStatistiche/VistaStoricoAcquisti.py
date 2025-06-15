from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QTableWidget, QHeaderView, \
    QTableWidgetItem, QMessageBox

from Gestori.GestoreStatistiche import GestoreStatistiche

class VistaStoricoAcquisti(QWidget):

    def __init__(self):
        try:
            super().__init__()

            self.setWindowTitle("VideoSpace")
            self.setFixedSize(1000, 600)

            font = QFont("impact", 20)

            layout = QVBoxLayout()

            label_titolo = QLabel("Storico acquisti")
            label_titolo.setFont(font)
            layout.addWidget(label_titolo)

            self.tabella = QTableWidget()
            self.tabella.setColumnCount(7)
            self.tabella.setHorizontalHeaderLabels(
                ["Id ricevuta", "Prodotto acquistato", "Nome cliente", "Cognome cliente", "Id cliente", "Data di acquisto", "Importo"])
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
            acquisti = gestore_statistiche.storicoAcquisti()

            self.popola_tabella(acquisti)
        except Exception as e:
            print(e)

    def popola_tabella(self, ricevute_filtrate):

        self.tabella.setRowCount(len(ricevute_filtrate))

        for row, ricevuta in enumerate(ricevute_filtrate):
            self.tabella.setItem(row, 0, QTableWidgetItem(str(ricevuta.getId())))
            self.tabella.setItem(row, 1, QTableWidgetItem(ricevuta.prodotto.nome))
            self.tabella.setItem(row, 2, QTableWidgetItem(ricevuta.cliente.nome))
            self.tabella.setItem(row, 3, QTableWidgetItem(ricevuta.cliente.cognome))
            self.tabella.setItem(row, 4, QTableWidgetItem(str(ricevuta.cliente.id)))
            self.tabella.setItem(row, 5, QTableWidgetItem(str(ricevuta.dataEmissione)))
            self.tabella.setItem(row, 6, QTableWidgetItem(str(ricevuta.importo)))

        # Se la lista è vuota la tabella viene resettata
        if not ricevute_filtrate:
            self.tabella.setRowCount(0)
            QMessageBox.information(self, 'Attenzione', 'Non sono ancora stati registrati acquisti', QMessageBox.Ok)
            self.close()
            return

    def on_click_indietro(self):
        from Viste.GestioneStatistiche.VistaStatistiche import VistaStatistiche
        self.vista_statistiche = VistaStatistiche()
        self.vista_statistiche.show()
        self.close()