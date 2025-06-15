from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

from Viste.GestioneProdotti.VistaModificaFilm import VistaModificaFilm

class VistaGestioneFilm(QWidget):
    def __init__(self, film):
        try:
            super().__init__()

            self.film = film

            self.setWindowTitle("VideoSpace")
            self.setFixedSize(600, 600)

            font = QFont("impact", 20)
            font2 = QFont("MS Shell Dlg 2", 10)

            layout = QVBoxLayout()

            label_titolo = QLabel("Gestione film")
            label_titolo.setFont(font)
            layout.addWidget(label_titolo)

            layout.addSpacing(20)

            label_nome = QLabel("Nome: " + film.nome)
            label_nome.setFont(font2)
            layout.addWidget(label_nome)

            label_id = QLabel("Id: " + str(film.id))
            label_id.setFont(font2)
            layout.addWidget(label_id)

            label_anno = QLabel("Anno: " + str(film.anno))
            label_anno.setFont(font2)
            layout.addWidget(label_anno)

            label_genere = QLabel("Genere: " + film.genereFilm)
            label_genere.setFont(font2)
            layout.addWidget(label_genere)

            label_prezzo_acquisto = QLabel("Prezzo acquisto: €" + str(film.costoAcquisto))
            label_prezzo_acquisto.setFont(font2)
            layout.addWidget(label_prezzo_acquisto)

            label_prezzo_noleggio = QLabel("Prezzo noleggio: €" + str(film.costoNoleggio))
            label_prezzo_noleggio.setFont(font2)
            layout.addWidget(label_prezzo_noleggio)

            label_unita = QLabel("Unità: " + str(film.unita))
            label_unita.setFont(font2)
            layout.addWidget(label_unita)

            label_regista = QLabel("Regista: " + film.regista)
            label_regista.setFont(font2)
            layout.addWidget(label_regista)

            layout.addSpacing(20)

            layout_pulsanti = QHBoxLayout()
            layout_pulsanti.setAlignment(Qt.AlignCenter)

            self.aggiungi_pulsante("Modifica", layout_pulsanti, self.on_click_modifica)
            self.aggiungi_pulsante("Rimuovi", layout_pulsanti, self.on_click_rimuovi)
            self.aggiungi_pulsante("Indietro", layout_pulsanti, self.on_click_indietro)

            layout.addLayout(layout_pulsanti)

            self.setLayout(layout)
        except Exception as e:
            print(e)

    def aggiungi_pulsante(self, nome, layout, azione):
        pulsante = QPushButton(nome)
        layout.addWidget(pulsante)
        layout.addSpacing(20)
        pulsante.clicked.connect(azione)

    def on_click_modifica(self):
        self.vista_modifica_film = VistaModificaFilm(self.film)
        self.vista_modifica_film.show()
        self.close()

    def on_click_indietro(self):
        from Viste.GestioneProdotti.VistaProdotti import VistaProdotti
        self.vista_prodotti = VistaProdotti()
        self.vista_prodotti.show()
        self.close()

    def on_click_rimuovi(self):
        try:
            from Viste.GestioneProdotti.VistaRimozioneProdotto import VistaRimozioneProdotto
            self.vista_rimozione_prodotto = VistaRimozioneProdotto("film", self.film, self)
            self.vista_rimozione_prodotto.show()
        except Exception as e:
            print(e)