import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy

from Viste.GestioneServizi.VistaAcquisto import VistaAcquisto
from Viste.GestioneClienti.VistaClienti import VistaClienti
from Viste.GestioneServizi.VistaNoleggio import VistaNoleggio
from Viste.GestioneProdotti.VistaProdotti import VistaProdotti
from Viste.GestioneStatistiche.VistaStatistiche import VistaStatistiche

class VistaHome(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VideoSpace")
        self.setFixedSize(600, 600)

        self.font = QFont("impact", 20)

        logo_layout = QVBoxLayout()
        logo_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        container_logo = QLabel()
        
        image_path = os.path.join("src", "Logo.png")
        logo = QPixmap(image_path)

        if logo.isNull():
            print(f"ATTENZIONE: Impossibile caricare l'immagine dal percorso '{image_path}'")
            container_logo.setText("Logo non trovato")
        else:
            container_logo.setPixmap(logo.scaledToWidth(400))

        container_logo.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        logo_layout.addWidget(container_logo)

        main_layout = QVBoxLayout()
        main_layout.addLayout(logo_layout)

        button_layout = QHBoxLayout()

        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()

        self.aggiungi_pulsante("Acquisto", layout1, self.on_click_acquisto)

        layout1.addSpacing(20)

        self.aggiungi_pulsante("Prodotti", layout1, self.on_click_prodotti)

        layout1.addSpacing(20)

        self.aggiungi_pulsante("Statistiche", layout1, self.on_click_statistiche)

        self.aggiungi_pulsante("Noleggio", layout2, self.on_click_noleggio)

        layout2.addSpacing(20)

        self.aggiungi_pulsante("Clienti", layout2, self.on_click_clienti)

        layout2.addSpacing(20)

        self.aggiungi_pulsante("Esci", layout2, self.on_click_esci)

        button_layout.addLayout(layout1)
        button_layout.addLayout(layout2)

        main_layout.addLayout(button_layout)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(main_layout)

    def aggiungi_pulsante(self, nome, layout, azione):
        pulsante = QPushButton(nome)
        pulsante.setFont(self.font)
        layout.addWidget(pulsante)
        pulsante.clicked.connect(azione)

    def on_click_acquisto(self):
        self.vista_acquisto = VistaAcquisto()
        self.vista_acquisto.show()
        self.close()

    def on_click_noleggio(self):
        self.vista_noleggio = VistaNoleggio()
        self.vista_noleggio.show()
        self.close()

    def on_click_prodotti(self):
        self.vista_prodotti = VistaProdotti()
        self.vista_prodotti.show()
        self.close()

    def on_click_clienti(self):
        self.vista_clienti = VistaClienti()
        self.vista_clienti.show()
        self.close()

    def on_click_statistiche(self):
        self.vista_statistiche = VistaStatistiche()
        self.vista_statistiche.show()
        self.close()

    def on_click_esci(self):
        self.close()