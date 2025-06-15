from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

from Viste.GestioneProdotti.VistaModificaVideogioco import VistaModificaVideogioco

class VistaGestioneVideogioco(QWidget):
    def __init__(self, videogioco):
        super().__init__()

        self.videogioco = videogioco

        self.setWindowTitle("VideoSpace")
        self.setFixedSize(600, 600)

        font = QFont("impact", 20)
        font2 = QFont("MS Shell Dlg 2", 10)

        layout = QVBoxLayout()

        label_titolo = QLabel("Gestione videogioco")
        label_titolo.setFont(font)
        layout.addWidget(label_titolo)

        layout.addSpacing(20)

        label_nome = QLabel("Nome: " + videogioco.nome)
        label_nome.setFont(font2)
        layout.addWidget(label_nome)

        label_id = QLabel("Id: " + str(videogioco.id))
        label_id.setFont(font2)
        layout.addWidget(label_id)

        label_anno = QLabel("Anno: " + str(videogioco.anno))
        label_anno.setFont(font2)
        layout.addWidget(label_anno)

        label_genere = QLabel("Genere: " + videogioco.genereVideogioco)
        label_genere.setFont(font2)
        layout.addWidget(label_genere)

        label_prezzo_acquisto = QLabel("Prezzo acquisto: €" + str(videogioco.costoAcquisto))
        label_prezzo_acquisto.setFont(font2)
        layout.addWidget(label_prezzo_acquisto)

        label_prezzo_noleggio = QLabel("Prezzo noleggio: €" + str(videogioco.costoNoleggio))
        label_prezzo_noleggio.setFont(font2)
        layout.addWidget(label_prezzo_noleggio)

        label_unita = QLabel("Unità: " + str(videogioco.unita))
        label_unita.setFont(font2)
        layout.addWidget(label_unita)

        label_piattaforma = QLabel("Piattaforma: " + videogioco.piattaforma)
        label_piattaforma.setFont(font2)
        layout.addWidget(label_piattaforma)

        layout.addSpacing(20)

        layout_pulsanti = QHBoxLayout()
        layout_pulsanti.setAlignment(Qt.AlignCenter)

        self.aggiungi_pulsante("Modifica", layout_pulsanti, self.on_click_modifica)
        self.aggiungi_pulsante("Rimuovi", layout_pulsanti, self.on_click_rimuovi)
        self.aggiungi_pulsante("Indietro", layout_pulsanti, self.on_click_indietro)

        layout.addLayout(layout_pulsanti)

        self.setLayout(layout)

    def aggiungi_pulsante(self, nome, layout, azione):
        pulsante = QPushButton(nome)
        layout.addWidget(pulsante)
        layout.addSpacing(20)
        pulsante.clicked.connect(azione)

    def on_click_modifica(self):
        self.vista_modifica_videogioco = VistaModificaVideogioco(self.videogioco)
        self.vista_modifica_videogioco.show()
        self.close()

    def on_click_indietro(self):
        from Viste.GestioneProdotti.VistaProdotti import VistaProdotti
        self.vista_prodotti = VistaProdotti()
        self.vista_prodotti.show()
        self.close()

    def on_click_rimuovi(self):
        try:
            from Viste.GestioneProdotti.VistaRimozioneProdotto import VistaRimozioneProdotto
            self.vista_rimozione_prodotto = VistaRimozioneProdotto("videogioco", self.videogioco, self)
            self.vista_rimozione_prodotto.show()
        except Exception as e:
            print(e)