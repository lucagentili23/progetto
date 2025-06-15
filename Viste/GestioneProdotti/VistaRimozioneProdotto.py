from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QMessageBox

class VistaRimozioneProdotto(QWidget):
    def __init__(self, tipo, prodotto, parent_window):
        try:
            super().__init__()

            self.prodotto = prodotto
            self.tipo = tipo
            self.parent_window = parent_window

            self.setFixedSize(500, 150)

            # rimuove i pulsanti di riduzione e ingrandimento
            self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)

            font_title = QFont("impact", 20)

            self.setWindowTitle("VideoSpace")

            layout = QVBoxLayout()

            label_titolo = QLabel("Rimozione prodotto")
            label_titolo.setFont(font_title)
            layout.addWidget(label_titolo)

            label_testo = QLabel("Sei sicuro di voler rimuovere il prodotto selezionato dal catalogo?")
            layout.addWidget(label_testo)

            layout_buttons = QHBoxLayout()

            self.aggiungi_pulsante("Conferma", layout_buttons, self.on_click_conferma)
            self.aggiungi_pulsante("Annulla", layout_buttons, self.on_click_annulla)

            layout_buttons.setAlignment(Qt.AlignCenter)

            layout.addLayout(layout_buttons)

            self.setLayout(layout)
        except Exception as e:
            print(e)

    def aggiungi_pulsante(self, nome, layout, azione):
        pulsante = QPushButton(nome)
        layout.addWidget(pulsante)
        pulsante.clicked.connect(azione)
    def on_click_annulla(self):
        self.close()

    def on_click_conferma(self):
        from Viste.GestioneProdotti.VistaProdotti import VistaProdotti
        self.rimuovi_prodotto()
        QMessageBox.information(self, 'Successo', 'Prodotto rimosso correttamente', QMessageBox.Ok)
        self.parent_window.close()
        self.close()
        self.vista_prodotti = VistaProdotti()
        self.vista_prodotti.show()

    def rimuovi_prodotto(self):
        from Gestori.GestoreProdotto import GestoreProdotto
        gestore_prodotto = GestoreProdotto()
        gestore_prodotto.rimuovi_prodotto(self.prodotto)