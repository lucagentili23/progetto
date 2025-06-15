from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QComboBox, \
    QPushButton, QMessageBox

from Classi.Film import Film
from Gestori.GestoreProdotto import GestoreProdotto

class VistaModificaFilm(QWidget):

    def __init__(self, film):
        try:
            super().__init__()

            self.film = film

            self.setWindowTitle("VideoSpace")
            self.setFixedSize(600, 600)

            font = QFont("impact", 20)

            layout = QVBoxLayout()

            label_titolo = QLabel("Modifica film")
            label_titolo.setFont(font)
            layout.addWidget(label_titolo)

            layout.addSpacing(20)

            layout2 = QHBoxLayout()

            label_nome = QLabel("Nome:")
            layout2.addWidget(label_nome)

            self.line_nome = QLineEdit()
            self.line_nome.setText(film.nome)
            self.line_nome.setFixedWidth(450)
            layout2.addWidget(self.line_nome)
            layout2.setAlignment(self.line_nome, Qt.AlignRight)

            layout.addLayout(layout2)

            layout3 = QHBoxLayout()

            label_anno = QLabel("Anno:")
            layout3.addWidget(label_anno)

            self.line_anno = QLineEdit()
            self.line_anno.setText(str(film.anno))
            self.line_anno.setFixedWidth(450)
            layout3.addWidget(self.line_anno)
            layout3.setAlignment(self.line_anno, Qt.AlignRight)

            layout.addLayout(layout3)

            layout4 = QHBoxLayout()

            label_genere = QLabel("Genere:")
            layout4.addWidget(label_genere)

            self.combo_genere = QComboBox()
            self.combo_genere.setFixedWidth(450)
            self.combo_genere.addItems(["Azione", "Commedia", "Drammatico", "Horror", "Fantascienza", "Altro",
                                        "Thriller", "Avventura", "Animazione", "Documentario", "Romantico", "Fantasy"])
            self.combo_genere.setCurrentText(film.genereFilm)
            layout4.addWidget(self.combo_genere)
            layout4.setAlignment(self.combo_genere, Qt.AlignRight)

            layout.addLayout(layout4)

            layout5 = QHBoxLayout()

            label_prezzo_acquisto = QLabel("Prezzo Acquisto:")
            layout5.addWidget(label_prezzo_acquisto)

            self.line_prezzo_acquisto = QLineEdit()
            self.line_prezzo_acquisto.setText(str(film.costoAcquisto))
            self.line_prezzo_acquisto.setFixedWidth(450)
            layout5.addWidget(self.line_prezzo_acquisto)
            layout5.setAlignment(self.line_prezzo_acquisto, Qt.AlignRight)

            layout.addLayout(layout5)

            layout6 = QHBoxLayout()

            label_prezzo_noleggio = QLabel("Prezzo Noleggio:")
            layout6.addWidget(label_prezzo_noleggio)

            self.line_prezzo_noleggio = QLineEdit()
            self.line_prezzo_noleggio.setText(str(film.costoNoleggio))
            self.line_prezzo_noleggio.setFixedWidth(450)
            layout6.addWidget(self.line_prezzo_noleggio)
            layout6.setAlignment(self.line_prezzo_noleggio, Qt.AlignRight)

            layout.addLayout(layout6)

            layout7 = QHBoxLayout()

            label_unita = QLabel("Unità:")
            layout7.addWidget(label_unita)

            self.line_unita = QLineEdit()
            self.line_unita.setText(str(film.unita))
            self.line_unita.setFixedWidth(450)
            layout7.addWidget(self.line_unita)
            layout7.setAlignment(self.line_unita, Qt.AlignRight)

            layout.addLayout(layout7)

            layout9 = QHBoxLayout()

            label_regista = QLabel("Regista:")
            layout9.addWidget(label_regista)

            self.line_regista = QLineEdit()
            self.line_regista.setText(film.regista)
            self.line_regista.setFixedWidth(450)
            layout9.addWidget(self.line_regista)
            layout9.setAlignment(self.line_regista, Qt.AlignRight)

            layout.addLayout(layout9)

            layout.addSpacing(20)

            layout10 = QHBoxLayout()

            layout10.setAlignment(Qt.AlignCenter)

            self.aggiungi_pulsante("Conferma", layout10, self.on_click_conferma)
            layout10.addSpacing(20)
            self.aggiungi_pulsante("Annulla", layout10, self.on_click_annulla)

            layout.addLayout(layout10)

            spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            layout.addItem(spacer)

            self.setLayout(layout)
        except Exception as e:
            print(e)

    def aggiungi_pulsante(self, nome, layout, azione):
        pulsante = QPushButton(nome)
        pulsante.setFixedWidth(100)
        layout.addWidget(pulsante)
        pulsante.clicked.connect(azione)

    def on_click_annulla(self):
        try:
            from Viste.GestioneProdotti.VistaGestioneFilm import VistaGestioneFilm
            self.vista_gestione_film = VistaGestioneFilm(self.film)
            self.vista_gestione_film.show()
            self.close()
        except Exception as e:
            print(f"Errore durante l'apertura di VistaGestioneFilm: {e}")

    def on_click_conferma(self):
        try:
            nome = self.line_nome.text()
            anno = self.line_anno.text()
            genere = self.combo_genere.currentText()
            prezzo_acquisto = self.line_prezzo_acquisto.text()
            prezzo_noleggio = self.line_prezzo_noleggio.text()
            unita = int(self.line_unita.text())
            if unita > 0:
                disponibile = True
            else:
                disponibile = False
            regista = self.line_regista.text()

            film_modificato = Film(self.film.id, nome, anno, prezzo_acquisto, prezzo_noleggio, disponibile, unita, "Film", genere, regista)

            gestore_prodotto = GestoreProdotto()
            gestore_prodotto.modifica_prodotto(film_modificato)

            QMessageBox.information(self, 'Successo', 'Film modificato con successo', QMessageBox.Ok)

            from Viste.GestioneProdotti.VistaGestioneFilm import VistaGestioneFilm
            self.vista_gestione_film = VistaGestioneFilm(film_modificato)
            self.vista_gestione_film.show()
            self.close()
        except Exception as e:
            print(f"Errore durante la conferma: {e}")