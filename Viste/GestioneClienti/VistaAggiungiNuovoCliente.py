from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, \
    QPushButton, QMessageBox, QDateEdit

from Classi.Cliente import Cliente
from Gestori.GestoreCliente import GestoreCliente
from Gestori.GestoreProdotto import GestoreProdotto

class VistaAggiungiNuovoCliente(QWidget):
    def __init__(self):
        super().__init__()

        self.gestore_prodotto = GestoreProdotto()

        self.setWindowTitle("VideoSpace")
        self.setFixedSize(600, 600)

        font = QFont("impact", 20)

        layout = QVBoxLayout()

        label_titolo = QLabel("Aggiungi nuovo cliente")
        label_titolo.setFont(font)
        layout.addWidget(label_titolo)

        layout.addSpacing(20)

        layout2 = QHBoxLayout()

        label_nome = QLabel("Nome:")
        layout2.addWidget(label_nome)

        self.line_nome = QLineEdit()
        self.line_nome.setFixedWidth(450)
        layout2.addWidget(self.line_nome)
        layout2.setAlignment(self.line_nome, Qt.AlignRight)

        layout.addLayout(layout2)

        layout3 = QHBoxLayout()

        label_cognome = QLabel("Cognome:")
        layout3.addWidget(label_cognome)

        self.line_cognome = QLineEdit()
        self.line_cognome.setFixedWidth(450)
        layout3.addWidget(self.line_cognome)
        layout3.setAlignment(self.line_cognome, Qt.AlignRight)

        layout.addLayout(layout3)

        layout4 = QHBoxLayout()

        self.label_data = QLabel("Data di nascita:")
        layout4.addWidget(self.label_data)

        self.dateEdit = QDateEdit()
        self.dateEdit.setFixedWidth(450)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat('dd/MM/yyyy')
        self.dateEdit.setDate(QDate.currentDate())
        layout4.addWidget(self.dateEdit)
        layout4.setAlignment(self.dateEdit, Qt.AlignRight)

        layout.addLayout(layout4)

        layout5 = QHBoxLayout()

        label_luogo_nascita = QLabel("Luogo di nascita:")
        layout5.addWidget(label_luogo_nascita)

        self.line_luogo_nascita = QLineEdit()
        self.line_luogo_nascita.setFixedWidth(450)
        layout5.addWidget(self.line_luogo_nascita)
        layout5.setAlignment(self.line_luogo_nascita, Qt.AlignRight)

        layout.addLayout(layout5)

        layout6 = QHBoxLayout()

        label_codice_fiscale = QLabel("Codice fiscale:")
        layout6.addWidget(label_codice_fiscale)

        self.line_codice_fiscale = QLineEdit()
        self.line_codice_fiscale.setFixedWidth(450)
        layout6.addWidget(self.line_codice_fiscale)
        layout6.setAlignment(self.line_codice_fiscale, Qt.AlignRight)

        layout.addLayout(layout6)

        layout7 = QHBoxLayout()

        label_telefono = QLabel("Telefono:")
        layout7.addWidget(label_telefono)

        self.line_telefono = QLineEdit()
        self.line_telefono.setFixedWidth(450)
        layout7.addWidget(self.line_telefono)
        layout7.setAlignment(self.line_telefono, Qt.AlignRight)

        layout.addLayout(layout7)

        layout9 = QHBoxLayout()

        label_email = QLabel("Email:")
        layout9.addWidget(label_email)

        self.line_email = QLineEdit()
        self.line_email.setFixedWidth(450)
        layout9.addWidget(self.line_email)
        layout9.setAlignment(self.line_email, Qt.AlignRight)

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

        pulsante_conferma.clicked.connect(self.on_click_conferma)
        pulsante_annulla.clicked.connect(self.on_click_annulla)

        self.setLayout(layout)

    def on_click_conferma(self):
        if self.line_nome == "" or self.line_cognome == "" or self.line_email == "" or self.line_luogo_nascita == ""\
                or self.line_codice_fiscale == "" or self.line_telefono == "":
            QMessageBox.warning(self, 'Errore', 'Compila tutti i campi')
            return

        nome = self.line_nome.text()
        cognome = self.line_cognome.text()
        data = self.dateEdit.text()
        luogo = self.line_luogo_nascita.text()
        codice_fiscale = self.line_codice_fiscale.text()
        telefono = self.line_telefono.text()
        email = self.line_email.text()

        gestore_cliente = GestoreCliente()

        clienti = gestore_cliente.listaClienti

        for c in clienti:
            if c.codiceFiscale == codice_fiscale or c.email == email or c.numeroDiTelefono == telefono:
                QMessageBox.warning(self, 'Errore', 'Alcuni dei dati inseriti sono già associati ad un altro cliente')
                return

        cliente = Cliente(None, nome, cognome, codice_fiscale, data, email, luogo, telefono)

        gestore_cliente.aggiungi_cliente(cliente)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Operazione completata")
        msg.setText("Cliente registrato con successo.")
        msg.setStandardButtons(QMessageBox.Ok)

        # Esegue la finestra di dialogo e cattura la risposta
        retval = msg.exec_()

        # Se l'utente ha cliccato ok a quella finetsra 
        if retval == QMessageBox.Ok:
            from Viste.VistaHome import VistaHome
            self.vista_home = VistaHome()
            self.vista_home.show()
            self.close()

    def on_click_annulla(self):
        from Viste.GestioneClienti.VistaClienti import VistaClienti
        self.vista_clienti = VistaClienti()
        self.vista_clienti.show()
        self.close()