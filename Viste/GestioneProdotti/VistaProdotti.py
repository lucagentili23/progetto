from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QTableWidget, QHeaderView, \
    QComboBox, QTableWidgetItem, QMessageBox

from Classi.Film import Film
from Classi.Videogioco import Videogioco
from Viste.GestioneProdotti.VistaAggiungiNuovoProdotto import VistaAggiungiNuovoProdotto
from Viste.GestioneProdotti.VistaGestioneFilm import VistaGestioneFilm
from Gestori.GestoreProdotto import GestoreProdotto
from Viste.GestioneProdotti.VistaGestioneVideogioco import VistaGestioneVideogioco

class VistaProdotti(QWidget):

    def __init__(self):
        super().__init__()

        self.prodotti = []

        self.setWindowTitle("VideoSpace")
        self.setFixedSize(1000, 600)

        font = QFont("impact", 20)

        layout = QVBoxLayout()

        label_titolo = QLabel("Prodotti")
        label_titolo.setFont(font)
        layout.addWidget(label_titolo)

        layout1 = QHBoxLayout()
        layout1.setAlignment(Qt.AlignLeft)

        label_categoria = QLabel("Categoria:")
        layout1.addWidget(label_categoria)

        self.combo_categoria = QComboBox()
        self.combo_categoria.addItems(["Film", "Videogiochi"])
        layout1.addWidget(self.combo_categoria)

        layout1.addSpacing(50)

        label_ordina = QLabel("Ordina:")
        layout1.addWidget(label_ordina)

        self.combo_ordina = QComboBox()
        self.combo_ordina.addItems(["Nome (A-Z)", "Nome (Z-A)", "Anno (crescente)", "Anno (decrescente)",
                                    "Prezzo acquisto (crescente)", "Prezzo acquisto (decrescente)",
                                    "Prezzo noleggio (crescente)", "Prezzo noleggio (decrescente)"])
        layout1.addWidget(self.combo_ordina)

        layout1.addSpacing(50)

        label_genere = QLabel("Genere:")
        layout1.addWidget(label_genere)

        self.combo_genere_film = QComboBox()
        self.combo_genere_film.addItems(["Tutti", "Azione", "Commedia", "Drammatico", "Horror", "Fantascienza", "Altro",
                                         "Thriller", "Avventura", "Animazione", "Documentario", "Romantico", "Fantasy"])
        layout1.addWidget(self.combo_genere_film)

        self.combo_genere_videogiochi = QComboBox()
        self.combo_genere_videogiochi.addItems(["Tutti", "Azione", "Avventura", "RPG (Gioco di ruolo)", "Sparatutto",
                                                "Sportivo", "Simulazione", "Strategia", "Puzzle", "Musicale", "Horror"])
        layout1.addWidget(self.combo_genere_videogiochi)

        self.combo_categoria.currentIndexChanged.connect(self.on_categoria_changed)
        self.on_categoria_changed()

        layout1.addSpacing(50)

        pulsante_cerca = QPushButton("Cerca")
        layout1.addWidget(pulsante_cerca)

        layout.addLayout(layout1)

        self.tabella = QTableWidget()
        self.tabella.setColumnCount(7)
        self.tabella.setHorizontalHeaderLabels(["Nome", "Id", "Genere", "Anno", "Prezzo acquisto", "Prezzo noleggio", "Gestione"])
        self.tabella.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabella.verticalHeader().setVisible(False)

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

        bottone_aggiungi.clicked.connect(self.on_click_aggiungi_nuovo)
        pulsante_cerca.clicked.connect(self.on_click_cerca)
        bottone_indietro.clicked.connect(self.on_click_indietro)

        self.setLayout(layout)

        self.load_data()

    def on_categoria_changed(self):
        if self.combo_categoria.currentText() == "Film":
            self.combo_genere_film.show()
            self.combo_genere_videogiochi.hide()
        else:
            self.combo_genere_film.hide()
            self.combo_genere_videogiochi.show()

    def load_data(self):
        try:
            gestore_prodotto = GestoreProdotto()
            self.prodotti = gestore_prodotto.lista_prodotti
            self.ordina_prodotti(self.prodotti)
            prodotti_filtrati = self.filtra_prodotti(categoria="Film")
            self.aggiorna_tabella(prodotti_filtrati)
        except Exception as e:
            print(e)

    def on_click_aggiungi_nuovo(self):
        self.vista_aggiungi_nuovo_prodotto = VistaAggiungiNuovoProdotto()
        self.vista_aggiungi_nuovo_prodotto.show()
        self.close()

    def on_click_gestisci(self):
        global prod
        try:
            gestore_prodotto = GestoreProdotto()
            button = self.sender()
            if button:
                row = self.tabella.indexAt(button.pos()).row()
                id_prodotto = self.tabella.item(row, 1).text()

                for prodotto in gestore_prodotto.lista_prodotti:
                    if prodotto.getId() == int(id_prodotto):
                        prod = prodotto
                        if prod.getTipo() == "Film":
                            self.vista_gestione_film = VistaGestioneFilm(prod)
                            self.vista_gestione_film.show()
                        elif prod.getTipo() == "Videogioco":
                            self.vista_gestione_videogioco = VistaGestioneVideogioco(prod)
                            self.vista_gestione_videogioco.show()
                        self.close()
                        break
        except Exception as e:
            print(e)

    def on_click_cerca(self):
        categoria = self.combo_categoria.currentText()
        if categoria == "Film":
            genere_selezionato = self.combo_genere_film.currentText()
        else:  # Videogiochi
            genere_selezionato = self.combo_genere_videogiochi.currentText()
            categoria = "Videogioco"

        prodotti_filtrati = self.filtra_prodotti(categoria, genere_selezionato)
        ord = self.ordina_prodotti(prodotti_filtrati) 
        self.aggiorna_tabella(ord)

    def ordina_prodotti(self, prodotti):
        try:
            ordine = self.combo_ordina.currentText()
            if ordine == "Nome (A-Z)":
                prodotti.sort(key=lambda x: x.getNome())
            elif ordine == "Nome (Z-A)":
                prodotti.sort(key=lambda x: x.getNome(), reverse=True)
            elif ordine == "Anno (crescente)":
                prodotti.sort(key=lambda x: self.safe_int(x.getAnno()))
            elif ordine == "Anno (decrescente)":
                prodotti.sort(key=lambda x: self.safe_int(x.getAnno()), reverse=True)
            elif ordine == "Prezzo acquisto (crescente)":
                prodotti.sort(key=lambda x: x.getCostoAcquisto())
            elif ordine == "Prezzo acquisto (decrescente)":
                prodotti.sort(key=lambda x: x.getCostoAcquisto(), reverse=True)
            elif ordine == "Prezzo noleggio (crescente)":
                prodotti.sort(key=lambda x: x.getCostoNoleggio())
            elif ordine == "Prezzo noleggio (decrescente)":
                prodotti.sort(key=lambda x: x.getCostoNoleggio(), reverse=True)
            return prodotti
        except Exception as e:
            print(e)

    def safe_int(self, val):
        try:
            return int(val)
        except (ValueError, TypeError):
            return float('inf')

    def filtra_prodotti(self, categoria, genere_selezionato="Tutti"):
        try:
            prodotti_filtrati = []

            for prodotto in self.prodotti:
                if prodotto.getTipo() == categoria:
                    if genere_selezionato == "Tutti":
                        prodotti_filtrati.append(prodotto)
                    elif isinstance(prodotto, Film) and prodotto.getGenereFilm() == genere_selezionato:
                        prodotti_filtrati.append(prodotto)
                    elif isinstance(prodotto, Videogioco) and prodotto.getGenereVideogioco() == genere_selezionato:
                        prodotti_filtrati.append(prodotto)

            return prodotti_filtrati
        except Exception as e:
            print(f'c:{e}')

    def aggiorna_tabella(self, prodotti_filtrati):
        try:
            self.tabella.setRowCount(len(prodotti_filtrati))

            for row, prodotto in enumerate(prodotti_filtrati):
                self.tabella.setItem(row, 0, QTableWidgetItem(prodotto.getNome()))
                self.tabella.setItem(row, 1, QTableWidgetItem(str(prodotto.getId())))

                # Determina il genere in base al tipo di prodotto
                genere = ""
                if isinstance(prodotto, Film):
                    genere = prodotto.getGenereFilm()
                elif isinstance(prodotto, Videogioco):
                    genere = prodotto.getGenereVideogioco()

                self.tabella.setItem(row, 2, QTableWidgetItem(genere))
                self.tabella.setItem(row, 3, QTableWidgetItem(str(prodotto.getAnno())))
                self.tabella.setItem(row, 4, QTableWidgetItem(str(prodotto.getCostoAcquisto())))
                self.tabella.setItem(row, 5, QTableWidgetItem(str(prodotto.getCostoNoleggio())))

                btn_gestisci = QPushButton("Gestisci")
                btn_gestisci.clicked.connect(self.on_click_gestisci)
                self.tabella.setCellWidget(row, 6, btn_gestisci)

            if not self.prodotti:
                self.tabella.setRowCount(0)
                QMessageBox.information(self, 'Attenzione', 'Non sono presenti prodotti nel catalogo', QMessageBox.Ok)
                self.close()
        except Exception as e:
            print(e)

    def on_click_indietro(self):
        from Viste.VistaHome import VistaHome
        self.vista_home = VistaHome()
        self.vista_home.show()
        self.close()