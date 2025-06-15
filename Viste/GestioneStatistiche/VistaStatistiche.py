from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy

from Viste.GestioneStatistiche.VistaNoleggiInCorso import VistaNoleggiInCorso
from Viste.GestioneStatistiche.VistaStoricoAcquisti import VistaStoricoAcquisti
from Viste.GestioneStatistiche.VistaStoricoNoleggi import VistaStoricoNoleggi

class VistaStatistiche(QWidget):

    def __init__(self):
        try:
            super().__init__()

            self.setWindowTitle("VideoSpace")
            self.setFixedSize(600, 600)

            self.font = QFont("impact", 20)

            self.layout = QVBoxLayout()
            self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

            container_logo = QLabel()
            logo = QPixmap("src/Logo.png")
            container_logo.setPixmap(logo.scaledToWidth(400))
            container_logo.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            self.layout.addWidget(container_logo)

            self.aggiungi_pulsante("Storico acquisti", self.on_click_storico_acquisti)
            self.aggiungi_pulsante("Storico noleggi", self.on_click_storico_noleggi)
            self.aggiungi_pulsante("Noleggi in corso", self.on_click_noleggi_in_corso)
            self.aggiungi_pulsante("Indietro", self.on_click_indietro)

            self.setLayout(self.layout)
        except Exception as e:
            print(e)

    def aggiungi_pulsante(self, nome, azione):
        button_layout = QHBoxLayout()
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        button = QPushButton(nome)
        button.setFixedWidth(300)
        button.setFont(self.font)
        button.clicked.connect(azione)
        button_layout.addWidget(button)
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.layout.addLayout(button_layout)
        return button

    def on_click_storico_acquisti(self):
        self.vista_storico_acquiti = VistaStoricoAcquisti()
        self.vista_storico_acquiti.show()
        self.close()

    def on_click_storico_noleggi(self):
        self.vista_storico_noleggi = VistaStoricoNoleggi()
        self.vista_storico_noleggi.show()
        self.close()

    def on_click_noleggi_in_corso(self):
        self.vista_situazione_clienti = VistaNoleggiInCorso()
        self.vista_situazione_clienti.show()
        self.close()

    def on_click_indietro(self):
        from Viste.VistaHome import VistaHome
        self.vista_home = VistaHome()
        self.vista_home.show()
        self.close()