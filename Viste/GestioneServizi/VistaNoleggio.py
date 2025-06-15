import re
from datetime import datetime, timedelta

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, \
    QComboBox, QRadioButton, QListWidget, QButtonGroup, QMessageBox

from Classi.Film import Film
from Classi.Noleggio import Noleggio
from Classi.Ricevuta import Ricevuta
from Classi.Videogioco import Videogioco
from Gestori.GestoreCliente import GestoreCliente
from Gestori.GestoreNoleggio import GestoreNoleggio
from Gestori.GestoreProdotto import GestoreProdotto
from Gestori.GestoreRicevuta import GestoreRicevuta

class VistaNoleggio(QWidget):

    def __init__(self):
        super().__init__()

        self.prodotti = []
        self.clienti = []

        self.setWindowTitle("VideoSpace")
        self.setFixedSize(600, 600)

        font = QFont("impact", 20)

        layout = QVBoxLayout()

        label_acquisto = QLabel("Noleggio")
        label_acquisto.setFont(font)
        layout.addWidget(label_acquisto)

        layout1 = QHBoxLayout()

        self.cerca_prodotto = QLineEdit()
        self.cerca_prodotto.setPlaceholderText("Prodotto")
        layout1.addWidget(self.cerca_prodotto)

        self.combo_prodotto = QComboBox()
        self.combo_prodotto.addItems(["Nome", "id"])
        layout1.addWidget(self.combo_prodotto)

        self.radio_film = QRadioButton("Film")
        self.radio_videogioco = QRadioButton("Videogioco")

        radio_group = QButtonGroup()
        radio_group.addButton(self.radio_film)
        radio_group.addButton(self.radio_videogioco)

        layout1.addWidget(self.radio_film)
        layout1.addWidget(self.radio_videogioco)

        pulsante_cerca_prodotto = QPushButton("Cerca")
        pulsante_cerca_prodotto.setFixedWidth(50)
        layout1.addWidget(pulsante_cerca_prodotto)

        layout.addLayout(layout1)

        self.lista_prodotti = QListWidget()
        layout.addWidget(self.lista_prodotti)

        layout_durata = QHBoxLayout()

        label_durata = QLabel("Durata noleggio (giorni):")
        layout_durata.addWidget(label_durata)

        self.combo_durata = QComboBox()
        self.combo_durata.setFixedWidth(50)
        for i in range(2, 15):
            self.combo_durata.addItem(str(i))
        layout_durata.addWidget(self.combo_durata)

        spacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)
        layout_durata.addSpacerItem(spacer)

        self.label_costo = QLabel("Costo totale: €")
        layout_durata.addWidget(self.label_costo)

        layout_durata.addStretch()

        layout.addLayout(layout_durata)

        layout2 = QHBoxLayout()

        self.cerca_cliente = QLineEdit()
        self.cerca_cliente.setPlaceholderText("Cliente")
        layout2.addWidget(self.cerca_cliente)

        self.combo_cliente = QComboBox()
        self.combo_cliente.addItems(["Nome e cognome", "Codice fiscale", "Id"])
        layout2.addWidget(self.combo_cliente)

        pulsante_cerca_cliente = QPushButton("Cerca")
        pulsante_cerca_cliente.setFixedWidth(50)
        layout2.addWidget(pulsante_cerca_cliente)

        layout.addLayout(layout2)

        self.lista_clienti = QListWidget()
        layout.addWidget(self.lista_clienti)

        layout3 = QHBoxLayout()

        pulsante_conferma = QPushButton("Conferma")
        pulsante_conferma.setFixedWidth(200)
        layout3.addWidget(pulsante_conferma)

        layout3.addSpacing(40)

        pulsante_annulla = QPushButton("Annulla")
        pulsante_annulla.setFixedWidth(200)
        layout3.addWidget(pulsante_annulla)

        layout.addLayout(layout3)

        pulsante_annulla.clicked.connect(self.on_click_annulla)
        pulsante_cerca_prodotto.clicked.connect(self.on_click_cerca_prodotto)
        self.lista_prodotti.itemClicked.connect(self.on_select_prodotto)
        self.combo_durata.currentIndexChanged.connect(self.on_select_prodotto)
        self.radio_film.toggled.connect(self.on_check_film)
        self.radio_videogioco.toggled.connect(self.on_check_videogiochi)
        pulsante_conferma.clicked.connect(self.on_click_conferma)
        pulsante_cerca_cliente.clicked.connect(self.on_click_cerca_cliente)
        self.lista_prodotti.itemClicked.connect(self.on_item_clicked)

        self.lista_prodotti.setStyleSheet("""
                            QListWidget::item:selected {
                                background-color: #39afcc;
                            }
                        """)
        self.lista_clienti.setStyleSheet("""
                            QListWidget::item:selected {
                                background-color: #39afcc;
                            }
                        """)

        self.setLayout(layout)

    def on_click_annulla(self):
        from Viste.VistaHome import VistaHome
        self.vista_home = VistaHome()
        self.vista_home.show()
        self.close()

    def on_click_cerca_prodotto(self):
        try:
            if not self.radio_film.isChecked() and not self.radio_videogioco.isChecked():
                QMessageBox.warning(self, 'Errore', 'Seleziona la categoria')
                return
            if self.cerca_prodotto.text() == "":
                QMessageBox.warning(self, 'Errore', 'Inserisci i parametri di ricerca')
                return

            gestore_prodotto = GestoreProdotto()
            self.prodotti = gestore_prodotto.lista_prodotti

            self.lista_prodotti.clear()

            risultati = []

            if self.radio_film.isChecked():
                categoria = "Film"
            elif self.radio_videogioco.isChecked():
                categoria = "Videogioco"

            try:
                if self.combo_prodotto.currentText() == "Nome":
                    nome = self.cerca_prodotto.text()
                    for prodotto in self.prodotti:
                        if prodotto.tipo == categoria:
                            if nome in prodotto.nome:
                                risultati.append(prodotto)
                elif self.combo_prodotto.currentText() == "id":
                    id = self.cerca_prodotto.text()
                    for prodotto in self.prodotti:
                        if prodotto.tipo == categoria:
                            if str(id) in str(prodotto.id):
                                risultati.append(prodotto)
            except Exception as e:
                print(f"1:{e}")

            try:
                risultati_elaborati = []

                for r in risultati:
                    if self.radio_videogioco.isChecked():
                        if isinstance(r, Videogioco):
                            if r.disponibile:
                                res = str(r.id) + "  -  " + r.nome + "  -  " + r.piattaforma + "  -  €" + str(
                                    r.costoNoleggio) + "  -  Disponibile"
                            else:
                                res = str(r.id) + "  -  " + r.nome + "  -  " + r.piattaforma + "  -  €" + str(
                                    r.costoNoleggio) + "  -  Non disponibile"
                    if self.radio_film.isChecked():
                        if isinstance(r, Film):
                            if r.disponibile:
                                res = str(r.id) + "  -  " + r.nome + "  -  " + r.regista + "  -  €" + str(
                                    r.costoNoleggio) + "  -  Disponibile"
                            else:
                                res = str(r.id) + "  -  " + r.nome + "  -  " + r.regista + "  -  €" + str(
                                    r.costoNoleggio) + "  -  Non disponibile"
                    risultati_elaborati.append(res)

                self.lista_prodotti.addItems(risultati_elaborati)
            except Exception as e:
                print(f"2:{e}")
        except Exception as e:
            print(e)

    def on_item_clicked(self, item):
        if item.text().endswith("Non disponibile"):
            item.setSelected(False)

    def on_select_prodotto(self):
        try:
            elemento_selezionato = self.lista_prodotti.currentItem().text()
            match = re.match(r'(\d+)', elemento_selezionato)
            if not match:
                QMessageBox.warning(self, 'Errore', 'Errore nel matching del prodotto')
                return
            id_prodotto = int(match.group(1))
            prezzo = 0
            for prodotto in self.prodotti:
                if prodotto.id == id_prodotto:
                    prezzo = float(prodotto.costoNoleggio)
                    break

            durata = int(self.combo_durata.currentText())

            totale = prezzo * durata
            totale_arrotondato = round(totale, 2)

            self.label_costo.setText(f"Costo totale: €{totale_arrotondato}")
        except Exception as e:
            print(e)

    def on_check_film(self):
        if self.radio_film.isChecked():
            self.combo_durata.setEnabled(False)
            self.lista_prodotti.clear()
            self.combo_durata.setCurrentIndex(0)
            self.label_costo.setText("Costo totale: €")

    def on_check_videogiochi(self):
        if self.radio_videogioco.isChecked():
            self.combo_durata.setEnabled(True)
            self.lista_prodotti.clear()
            self.combo_durata.setCurrentIndex(0)
            self.label_costo.setText("Costo totale: €")

    def on_click_cerca_cliente(self):
        try:
            if self.cerca_cliente.text() == "":
                QMessageBox.warning(self, 'Errore', 'Inserisci i parametri di ricerca')
                return

            gestore_cliente = GestoreCliente()
            self.clienti = gestore_cliente.listaClienti

            self.lista_clienti.clear()

            risultati = []

            if self.combo_cliente.currentText() == "Nome e cognome":
                nome_e_cognome = self.cerca_cliente.text()
                for cliente in self.clienti:
                    s = cliente.nome + " " + cliente.cognome
                    if nome_e_cognome in s:
                        risultati.append(cliente)
            elif self.combo_cliente.currentText() == "Codice fiscale":
                codice_fiscale = self.cerca_cliente.text()
                for cliente in self.clienti:
                    if codice_fiscale in cliente.codiceFiscale:
                        risultati.append(cliente)
            elif self.combo_cliente.currentText() == "Id":
                try:
                    id = self.cerca_cliente.text()
                    for cliente in self.clienti:
                        if str(id) in str(cliente.id):
                            risultati.append(cliente)
                except Exception as e:
                    print(f"errore: {e}")

            risultati_elaborati = []

            for r in risultati:
                res = str(r.id) + "  -  " + r.nome + " " + r.cognome + "  -  " + r.codiceFiscale
                risultati_elaborati.append(res)

            self.lista_clienti.addItems(risultati_elaborati)

        except Exception as e:
            print(e)

    def on_click_conferma(self):

        prova1 = False
        prova2 = False
        prova3 = False

        try:
            # Verifica se è stato selezionato un prodotto
            if not self.lista_prodotti.selectedItems():
                QMessageBox.warning(self, 'Errore', 'Seleziona un prodotto')
                return

            # Verifica se è stato selezionato un cliente
            if not self.lista_clienti.selectedItems():
                QMessageBox.warning(self, 'Errore', 'Seleziona un cliente')
                return

            # Prendo l'id del prodotto selezionato
            prodotto_selezionato = self.lista_prodotti.selectedItems()[0].text()
            match = re.match(r'(\d+)', prodotto_selezionato)
            if not match:
                QMessageBox.warning(self, 'Errore', 'Errore nel matching del prodotto')
                return
            id_prodotto = int(match.group(1))

            # prendo l'id del cliente selezionato
            cliente_selezionato = self.lista_clienti.selectedItems()[0].text()
            match2 = re.match(r'(\d+)', cliente_selezionato)
            if not match2:
                QMessageBox.warning(self, 'Errore', 'Errore nel matching del cliente')
                return
            id_cliente = int(match2.group(1))

            prodotto_noleggiato = next((p for p in self.prodotti if p.id == id_prodotto), None)
            if not prodotto_noleggiato:
                QMessageBox.warning(self, 'Errore', 'Prodotto non trovato')
                return

            cliente_che_noleggia = next((c for c in self.clienti if c.id == id_cliente), None)
            if not cliente_che_noleggia:
                QMessageBox.warning(self, 'Errore', 'Cliente non trovato')
                return

            data_inizio = datetime.today()
            data_inizio_elaborata = data_inizio.strftime("%d-%m-%Y")
            durata = int(self.combo_durata.currentText())
            data_fine = data_inizio + timedelta(days=durata)
            data_fine_elaborata = data_fine.strftime("%d-%m-%Y")

            importo = float(prodotto_noleggiato.costoNoleggio) * durata
            tipologia = "Noleggio"

            noleggio = Noleggio(None, data_inizio_elaborata, data_fine_elaborata, importo, id_cliente, id_prodotto, False)

            try:
                gestore_noleggio = GestoreNoleggio()
                gestore_noleggio.aggiungi_noleggio(noleggio)
                id_noleggio = noleggio.id
                prova1 = True
            except Exception as e:
                print(f"b:{e}")

            ricevuta = Ricevuta(None, cliente_che_noleggia, data_inizio_elaborata, importo, prodotto_noleggiato, tipologia, id_noleggio)

            try:
                gestore_ricevuta = GestoreRicevuta()
                gestore_ricevuta.aggiungi_ricevuta(ricevuta)
                prodotto_noleggiato.unita -= 1
                gestore_prodotto = GestoreProdotto()
                gestore_prodotto.modifica_prodotto(prodotto_noleggiato)
                prova2 = True
            except Exception as e:
                print(f"a: {e}")

            prova3 = True

        except Exception as e:
            QMessageBox.critical(self, 'Errore', f"Si è verificato un errore: {str(e)}")
            print(e)

        if prova1 and prova2 and prova3:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Operazione completata")
            msg.setText("Noleggio effettuato con successo.")
            msg.setStandardButtons(QMessageBox.Ok)

            # Esegue finestra dialogo e cattura risposta
            retval = msg.exec_()

            if retval == QMessageBox.Ok:
                from Viste.VistaHome import VistaHome
                self.vista_home = VistaHome()
                self.vista_home.show()
                self.close()