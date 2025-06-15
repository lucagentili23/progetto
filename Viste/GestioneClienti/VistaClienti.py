from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QTableWidget, QHeaderView, QComboBox, QTableWidgetItem

from Gestori.GestoreCliente import GestoreCliente
from Viste.GestioneClienti.VistaAggiungiNuovoCliente import VistaAggiungiNuovoCliente
from Viste.GestioneClienti.VistaGestioneCliente import VistaGestioneCliente

class VistaClienti(QWidget):
    try:
        def __init__(self):
            super().__init__()

            self.clienti = []

            self.setWindowTitle("VideoSpace")
            self.setFixedSize(1000, 600)

            font = QFont("impact", 20)

            layout = QVBoxLayout()

            label_titolo = QLabel("Clienti")
            label_titolo.setFont(font)
            layout.addWidget(label_titolo)

            layout1 = QHBoxLayout()
            layout1.setAlignment(Qt.AlignLeft)

            label_categoria = QLabel("Ordina:")
            layout1.addWidget(label_categoria)

            self.combo_ordina = QComboBox()
            self.combo_ordina.addItems(["Cognome (A-Z)", "Cognome (Z-A)", "Data di nascita (crescente)", "Data di nascita (decrescente)"])
            layout1.addWidget(self.combo_ordina)

            layout1.addSpacing(50)

            pulsante_cerca = QPushButton("Cerca")
            layout1.addWidget(pulsante_cerca)

            layout.addLayout(layout1)

            self.tabella = QTableWidget()
            self.tabella.setColumnCount(9)
            self.tabella.setHorizontalHeaderLabels(
                ["Id", "Nome", "Cognome", "Data di nascita", "Luogo di nascita", "Codice fiscale", "Telefono", "Email", "Gestione"])
            self.tabella.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tabella.verticalHeader().setVisible(False)  # Nasconde i numeri nelle righe

            layout.addWidget(self.tabella)

            layout2 = QHBoxLayout()

            bottone_aggiungi = QPushButton("Aggiungi nuovo")
            bottone_aggiungi.setFixedWidth(200)
            layout2.addWidget(bottone_aggiungi)

            layout2.addSpacing(40)

            bottone_indietro = QPushButton("Indietro")
            bottone_indietro.setFixedWidth(200)
            layout2.addWidget(bottone_indietro)

            layout2.setAlignment(Qt.AlignCenter)

            layout.addLayout(layout2)

            bottone_aggiungi.clicked.connect(self.on_click_aggiungi)
            pulsante_cerca.clicked.connect(self.on_click_cerca)
            bottone_indietro.clicked.connect(self.on_click_indietro)

            self.setLayout(layout)

            self.load_data()
    except Exception as e:
        print(f"ee{e}")

    def load_data(self):
        gestore_clienti = GestoreCliente()
        self.clienti = gestore_clienti.listaClienti
        self.ordina_clienti(self.clienti)
        self.popola_tabella()

    def ordina_clienti(self, clienti):
        try:
            ordine = self.combo_ordina.currentText()

            if ordine == "Cognome (A-Z)":
                clienti.sort(key=lambda x: x.cognome)

            elif ordine == "Cognome (Z-A)":
                clienti.sort(key=lambda x: x.cognome, reverse=True)

            elif ordine == "Data di nascita (crescente)":
                clienti.sort(key=lambda x: datetime.strptime(x.dataDiNascita, '%d/%m/%Y'))

            elif ordine == "Data di nascita (decrescente)":
                clienti.sort(key=lambda x: datetime.strptime(x.dataDiNascita, '%d/%m/%Y'),
                             reverse=True)

        except Exception as e:
            print(f'Errore: {e}')

    def popola_tabella(self):
        self.tabella.setRowCount(len(self.clienti))
        for row, cliente in enumerate(self.clienti):
            self.tabella.setItem(row, 0, QTableWidgetItem(str(cliente.id)))
            self.tabella.setItem(row, 1, QTableWidgetItem(str(cliente.nome)))
            self.tabella.setItem(row, 2, QTableWidgetItem(str(cliente.cognome)))
            self.tabella.setItem(row, 3, QTableWidgetItem(str(cliente.dataDiNascita)))
            self.tabella.setItem(row, 4, QTableWidgetItem(str(cliente.luogoDiNascita)))
            self.tabella.setItem(row, 5, QTableWidgetItem(str(cliente.codiceFiscale)))
            self.tabella.setItem(row, 6, QTableWidgetItem(str(cliente.numeroDiTelefono)))
            self.tabella.setItem(row, 7, QTableWidgetItem(str(cliente.email)))

            btn_gestisci = QPushButton("Gestisci")
            btn_gestisci.clicked.connect(self.on_click_gestisci)
            self.tabella.setCellWidget(row, 8, btn_gestisci)

        # Se la lista è vuota la tabella viene resetttata
        if not self.clienti:
            self.tabella.setRowCount(0)

    def on_click_aggiungi(self):
        self.vista_aggiungi_nuovo_cliente = VistaAggiungiNuovoCliente()
        self.vista_aggiungi_nuovo_cliente.show()
        self.close()

    def on_click_cerca(self):
        self.load_data()

    def on_click_indietro(self):
        from Viste.VistaHome import VistaHome
        self.vista_home = VistaHome()
        self.vista_home.show()
        self.close()

    def on_click_gestisci(self):
        global cliente
        try:
            gestore_cliente = GestoreCliente()
            button = self.sender()
            if button:
                row = self.tabella.indexAt(button.pos()).row()
                id_cliente = self.tabella.item(row, 0).text()

                try:
                    id_cliente_int = int(id_cliente)
                except ValueError as e:
                    print(f"Errore: {e}")
                    return

                for c in gestore_cliente.listaClienti:
                    if c.id == id_cliente_int:
                        cliente = c
                        self.vista_gestione_cliente = VistaGestioneCliente(cliente)
                        self.vista_gestione_cliente.show()
                        self.close()
                        break
        except Exception as e:
            print(e)