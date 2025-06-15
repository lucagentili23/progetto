from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, \
    QComboBox, QRadioButton, QPushButton, QMessageBox

from Classi.Film import Film
from Classi.Videogioco import Videogioco
from Gestori.GestoreProdotto import GestoreProdotto

class VistaAggiungiNuovoProdotto(QWidget):

    def __init__(self):
        super().__init__()

        self.gestore_prodotto = GestoreProdotto()

        self.setWindowTitle("VideoSpace")
        self.setFixedSize(600, 600)

        font = QFont("impact", 20)

        layout = QVBoxLayout()

        label_titolo = QLabel("Aggiungi nuovo prodotto")
        label_titolo.setFont(font)
        layout.addWidget(label_titolo)

        layout.addSpacing(20)

        layout1 = QHBoxLayout()

        label_categoria = QLabel("Categoria:")
        layout1.addWidget(label_categoria)

        self.radio_film = QRadioButton("Film")
        layout1.addWidget(self.radio_film)

        self.radio_videogioco = QRadioButton("Videogioco")
        layout1.addWidget(self.radio_videogioco)

        layout.addLayout(layout1)

        layout2 = QHBoxLayout()

        label_nome = QLabel("Nome:")
        layout2.addWidget(label_nome)

        self.line_nome = QLineEdit()
        self.line_nome.setFixedWidth(450)
        layout2.addWidget(self.line_nome)
        layout2.setAlignment(self.line_nome, Qt.AlignRight)

        layout.addLayout(layout2)

        layout3 = QHBoxLayout()

        label_anno = QLabel("Anno:")
        layout3.addWidget(label_anno)

        self.line_anno = QLineEdit()
        self.line_anno.setFixedWidth(450)
        layout3.addWidget(self.line_anno)
        layout3.setAlignment(self.line_anno, Qt.AlignRight)

        layout.addLayout(layout3)

        layout4 = QHBoxLayout()

        self.label_genere = QLabel("Genere:")
        self.label_genere.hide()
        layout4.addWidget(self.label_genere)

        self.combo_genere_film = QComboBox()
        self.combo_genere_film.hide()
        self.combo_genere_film.setFixedWidth(450)
        self.combo_genere_film.addItems([
            "Azione", "Commedia", "Drammatico", "Horror", "Fantascienza", "Altro",
            "Thriller", "Avventura", "Animazione", "Documentario", "Romantico", "Fantasy"
        ])
        layout4.addWidget(self.combo_genere_film)
        layout4.setAlignment(self.combo_genere_film, Qt.AlignRight)

        self.combo_genere_videogioco = QComboBox()
        self.combo_genere_videogioco.hide()
        self.combo_genere_videogioco.setFixedWidth(450)
        self.combo_genere_videogioco.addItems([
            "Azione", "Avventura", "RPG (Gioco di ruolo)", "Sparatutto", "Sportivo",
            "Simulazione", "Strategia", "Puzzle", "Musicale", "Horror"
        ])
        layout4.addWidget(self.combo_genere_videogioco)
        layout4.setAlignment(self.combo_genere_videogioco, Qt.AlignRight)

        layout.addLayout(layout4)

        layout5 = QHBoxLayout()

        label_prezzo_acquisto = QLabel("Prezzo Acquisto:")
        layout5.addWidget(label_prezzo_acquisto)

        self.line_prezzo_acquisto = QLineEdit()
        self.line_prezzo_acquisto.setFixedWidth(450)
        layout5.addWidget(self.line_prezzo_acquisto)
        layout5.setAlignment(self.line_prezzo_acquisto, Qt.AlignRight)

        layout.addLayout(layout5)

        layout6 = QHBoxLayout()

        label_prezzo_noleggio = QLabel("Prezzo Noleggio:")
        layout6.addWidget(label_prezzo_noleggio)

        self.line_prezzo_noleggio = QLineEdit()
        self.line_prezzo_noleggio.setFixedWidth(450)
        layout6.addWidget(self.line_prezzo_noleggio)
        layout6.setAlignment(self.line_prezzo_noleggio, Qt.AlignRight)

        layout.addLayout(layout6)

        layout7 = QHBoxLayout()

        label_unita = QLabel("Unità:")
        layout7.addWidget(label_unita)

        self.line_unita = QLineEdit()
        self.line_unita.setFixedWidth(450)
        layout7.addWidget(self.line_unita)
        layout7.setAlignment(self.line_unita, Qt.AlignRight)

        layout.addLayout(layout7)

        layout8 = QHBoxLayout()

        self.label_piattaforma = QLabel("Piattaforma:")
        self.label_piattaforma.hide()
        layout8.addWidget(self.label_piattaforma)

        self.combo_piattaforma = QComboBox()
        self.combo_piattaforma.hide()
        self.combo_piattaforma.setFixedWidth(450)
        piattaforme = [
            "PlayStation 5", "PlayStation 4", "PlayStation 3",
            "PlayStation 2", "PlayStation 1",
            "Xbox Series X", "Xbox Series S", "Xbox One",
            "Nintendo Switch", "Nintendo Wii U", "Nintendo 3DS",
            "PC"
        ]
        self.combo_piattaforma.addItems(piattaforme)
        layout8.addWidget(self.combo_piattaforma)
        layout8.setAlignment(self.combo_piattaforma, Qt.AlignRight)

        layout.addLayout(layout8)

        layout9 = QHBoxLayout()

        self.label_regista = QLabel("Regista:")
        self.label_regista.hide()
        layout9.addWidget(self.label_regista)

        self.line_regista = QLineEdit()
        self.line_regista.hide()
        self.line_regista.setFixedWidth(450)
        layout9.addWidget(self.line_regista)
        layout9.setAlignment(self.line_regista, Qt.AlignRight)

        layout.addLayout(layout9)

        layout.addSpacing(20)

        layout10 = QHBoxLayout()

        layout10.setAlignment(Qt.AlignCenter)

        pulsante_conferma = QPushButton("Conferma")
        pulsante_conferma.setFixedWidth(100)
        layout10.addWidget(pulsante_conferma)

        layout10.addSpacing(20)

        pulsante_annulla = QPushButton("Annulla")
        pulsante_annulla.setFixedWidth(100)
        layout10.addWidget(pulsante_annulla)

        layout.addLayout(layout10)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        self.radio_film.toggled.connect(self.on_check_radio)
        self.radio_videogioco.toggled.connect(self.on_check_radio)
        pulsante_conferma.clicked.connect(self.on_click_conferma)
        pulsante_annulla.clicked.connect(self.show_vista_prodotti)

        self.setLayout(layout)

    def on_check_radio(self):
        if self.radio_film.isChecked():
            self.label_regista.show()
            self.line_regista.show()
            self.label_piattaforma.hide()
            self.combo_piattaforma.hide()
            self.label_genere.show()
            self.combo_genere_film.show()
            self.combo_genere_videogioco.hide()
        if self.radio_videogioco.isChecked():
            self.label_piattaforma.show()
            self.combo_piattaforma.show()
            self.label_regista.hide()
            self.line_regista.hide()
            self.label_genere.show()
            self.combo_genere_videogioco.show()
            self.combo_genere_film.hide()

    def on_click_conferma(self):

        try:
            if self.radio_film.isChecked():
                if (self.line_nome.text() == "" or self.line_anno.text() == "" or self.line_prezzo_acquisto.text() == ""
                        or self.line_prezzo_noleggio.text() == "" or self.line_unita.text() == "" or self.line_regista.text() == ""):
                    QMessageBox.warning(self, 'Errore', 'Compila tutti i campi')
                    return

                nome = self.line_nome.text()
                anno = self.line_anno.text()
                genere = self.combo_genere_film.currentText()
                prezzo_acquisto = float(self.line_prezzo_acquisto.text())
                prezzo_noleggio = float(self.line_prezzo_noleggio.text())
                unita = int(self.line_unita.text())
                regista = self.line_regista.text()

                film = Film(None, nome, anno, prezzo_acquisto, prezzo_noleggio, True, unita, "Film", genere, regista)

                try:
                    self.gestore_prodotto.aggiungi_film(film)
                    QMessageBox.information(self, 'Successo', 'Film aggiunto con successo', QMessageBox.Ok)
                except Exception as e:
                    QMessageBox.critical(self, 'Errore', f'Errore durante l\'aggiunta del film: {str(e)}')

            elif self.radio_videogioco.isChecked():
                try:
                    if (self.line_nome.text() == "" or self.line_anno.text() == "" or self.line_prezzo_acquisto.text() == ""
                            or self.line_prezzo_noleggio.text() == "" or self.line_unita.text() == ""):
                        QMessageBox.warning(self, 'Errore', 'Compila tutti i campi')
                        return

                    nome = self.line_nome.text()
                    anno = self.line_anno.text()
                    genere = self.combo_genere_videogioco.currentText()
                    prezzo_acquisto = float(self.line_prezzo_acquisto.text())
                    prezzo_noleggio = float(self.line_prezzo_noleggio.text())
                    unita = int(self.line_unita.text())
                    piattaforma = self.combo_piattaforma.currentText()

                    videogioco = Videogioco(None, nome, anno, prezzo_acquisto, prezzo_noleggio, True, unita, "Videogioco", genere,
                                            piattaforma)

                    try:
                        self.gestore_prodotto.aggiungi_videogioco(videogioco)
                        QMessageBox.information(self, 'Successo', 'Videogioco aggiunto con successo', QMessageBox.Ok)
                    except Exception as e:
                        QMessageBox.critical(self, 'Errore', f'Errore durante l\'aggiunta del videogioco: {str(e)}')
                except Exception as e:
                    print(e)
            else:
                QMessageBox.warning(self, 'Errore', 'Compila tutti i campi')
                return

            self.show_vista_prodotti()
        except Exception as e:
            print(e)

    def show_vista_prodotti(self):
        from Viste.GestioneProdotti.VistaProdotti import VistaProdotti
        self.vista_prodotti = VistaProdotti()
        self.vista_prodotti.show()
        self.close()