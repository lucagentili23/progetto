from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

from Viste.GestioneClienti.VistaModificaCliente import VistaModificaCliente
from Viste.GestioneClienti.VistaRimozioneCliente import VistaRimozioneCliente

class VistaGestioneCliente(QWidget):
    def __init__(self, cliente):
        try:
            super().__init__()

            self.cliente = cliente

            self.setWindowTitle("VideoSpace")
            self.setFixedSize(600, 600)

            font = QFont("impact", 20)
            font2 = QFont("MS Shell Dlg 2", 10)

            layout = QVBoxLayout()

            label_titolo = QLabel("Gestione cliente")
            label_titolo.setFont(font)
            layout.addWidget(label_titolo)

            layout.addSpacing(20)

            try:
                label_id = QLabel("Id: " + str(cliente.id))
                label_id.setFont(font2)
                layout.addWidget(label_id)
            except Exception as e:
                print(e)

            try:
                label_nome = QLabel("Nome: " + str(cliente.nome))
                label_nome.setFont(font2)
                layout.addWidget(label_nome)
            except Exception as e:
                print(e)

            try:
                label_cognome = QLabel("Cognome: " + str(cliente.cognome))
                label_cognome.setFont(font2)
                layout.addWidget(label_cognome)
            except Exception as e:
                print(e)

            try:
                label_anno = QLabel("Data di nascita: " + str(cliente.dataDiNascita))
                label_anno.setFont(font2)
                layout.addWidget(label_anno)
            except Exception as e:
                print(e)

            try:
                label_genere = QLabel("Luogo di nascita: " + cliente.luogoDiNascita)
                label_genere.setFont(font2)
                layout.addWidget(label_genere)
            except Exception as e:
                print(e)

            try:
                label_codice_fiscale = QLabel("Codice fiscale: " + str(cliente.codiceFiscale))
                label_codice_fiscale.setFont(font2)
                layout.addWidget(label_codice_fiscale)
            except Exception as e:
                print(e)

            try:
                label_telefono = QLabel("Telefono: " + str(cliente.numeroDiTelefono))
                label_telefono.setFont(font2)
                layout.addWidget(label_telefono)
            except Exception as e:
                print(e)

            try:
                label_email = QLabel("Email: " + str(cliente.email))
                label_email.setFont(font2)
                layout.addWidget(label_email)
            except Exception as e:
                print(e)

            layout.addSpacing(20)

            layout_pulsanti = QHBoxLayout()
            layout_pulsanti.setAlignment(Qt.AlignCenter)

            self.aggiungi_pulsante("Modifica", layout_pulsanti, self.on_click_modifica)
            self.aggiungi_pulsante("Rimuovi", layout_pulsanti, self.on_click_rimuovi)
            self.aggiungi_pulsante("Indietro", layout_pulsanti, self.on_click_indietro)

            layout.addLayout(layout_pulsanti)

            self.setLayout(layout)
        except Exception as e:
            print(f"Unexpected error: {e}")

    def aggiungi_pulsante(self, nome, layout, azione):
        pulsante = QPushButton(nome)
        layout.addWidget(pulsante)
        layout.addSpacing(20)
        pulsante.clicked.connect(azione)

    def on_click_indietro(self):
        from Viste.GestioneClienti.VistaClienti import VistaClienti
        self.vista_clienti = VistaClienti()
        self.vista_clienti.show()
        self.close()

    def on_click_rimuovi(self):
        self.vista_rimozione_cliente = VistaRimozioneCliente(self.cliente, self)
        self.vista_rimozione_cliente.show()

    def on_click_modifica(self):
        self.vista_modifica_cliente = VistaModificaCliente(self.cliente)
        self.vista_modifica_cliente.show()
        self.close()