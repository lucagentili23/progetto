from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QPushButton, QDateEdit

from Classi.Cliente import Cliente
from Gestori.GestoreCliente import GestoreCliente

class VistaModificaCliente(QWidget):

    def __init__(self, cliente):
        try:
            super().__init__()

            self.cliente = cliente

            self.setWindowTitle("VideoSpace")
            self.setFixedSize(600, 600)

            font = QFont("impact", 20)

            layout = QVBoxLayout()

            label_titolo = QLabel("Modifica dati cliente")
            label_titolo.setFont(font)
            layout.addWidget(label_titolo)

            layout.addSpacing(20)

            layout2 = QHBoxLayout()

            label_nome = QLabel("Nome:")
            layout2.addWidget(label_nome)

            self.line_nome = QLineEdit()
            self.line_nome.setText(cliente.nome)
            self.line_nome.setFixedWidth(450)
            layout2.addWidget(self.line_nome)
            layout2.setAlignment(self.line_nome, Qt.AlignRight)

            layout.addLayout(layout2)

            layout3 = QHBoxLayout()

            label_cognome = QLabel("Cognome:")
            layout3.addWidget(label_cognome)

            self.line_cognome = QLineEdit()
            self.line_cognome.setText(cliente.cognome)
            self.line_cognome.setFixedWidth(450)
            layout3.addWidget(self.line_cognome)
            layout3.setAlignment(self.line_cognome, Qt.AlignRight)

            layout.addLayout(layout3)

            layout4 = QHBoxLayout()

            self.label_data = QLabel("Data di nascita:")
            layout4.addWidget(self.label_data)

            try:
                self.dateEdit = QDateEdit()
                self.dateEdit.setFixedWidth(450)
                self.dateEdit.setCalendarPopup(True)
                self.dateEdit.setDisplayFormat('dd/MM/yyyy')
                date_parts = cliente.dataDiNascita.split('/')
                date = QDate(int(date_parts[2]), int(date_parts[1]), int(date_parts[0]))
                self.dateEdit.setDate(date)
                layout4.addWidget(self.dateEdit)
                layout4.setAlignment(self.dateEdit, Qt.AlignRight)
            except Exception as e:
                print(f"er: {e}")

            layout.addLayout(layout4)

            layout5 = QHBoxLayout()

            label_luogo_nascita = QLabel("Luogo di nascita:")
            layout5.addWidget(label_luogo_nascita)

            self.line_luogo_nascita = QLineEdit()
            self.line_luogo_nascita.setText(cliente.luogoDiNascita)
            self.line_luogo_nascita.setFixedWidth(450)
            layout5.addWidget(self.line_luogo_nascita)
            layout5.setAlignment(self.line_luogo_nascita, Qt.AlignRight)

            layout.addLayout(layout5)

            layout6 = QHBoxLayout()

            label_codice_fiscale = QLabel("Codice fiscale:")
            layout6.addWidget(label_codice_fiscale)

            self.line_codice_fiscale = QLineEdit()
            self.line_codice_fiscale.setText(cliente.codiceFiscale)
            self.line_codice_fiscale.setFixedWidth(450)
            layout6.addWidget(self.line_codice_fiscale)
            layout6.setAlignment(self.line_codice_fiscale, Qt.AlignRight)

            layout.addLayout(layout6)

            layout7 = QHBoxLayout()

            label_telefono = QLabel("Telefono:")
            layout7.addWidget(label_telefono)

            self.line_telefono = QLineEdit()
            self.line_telefono.setText(cliente.numeroDiTelefono)
            self.line_telefono.setFixedWidth(450)
            layout7.addWidget(self.line_telefono)
            layout7.setAlignment(self.line_telefono, Qt.AlignRight)

            layout.addLayout(layout7)

            layout9 = QHBoxLayout()

            label_email = QLabel("Email:")
            layout9.addWidget(label_email)

            self.line_email = QLineEdit()
            self.line_email.setText(cliente.email)
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
        except Exception as e:
            print(e)

    def on_click_annulla(self):
        try:
            from Viste.GestioneClienti.VistaGestioneCliente import VistaGestioneCliente
            self.vista_gestione_cliente = VistaGestioneCliente(self.cliente)
            self.vista_gestione_cliente.show()
            self.close()
        except Exception as e:
            print(f"Errore durante l'apertura di VistaGestioneFilm: {e}")

    def on_click_conferma(self):
        try:
            id = self.cliente.id
            nome = self.line_nome.text()
            cognome = self.line_cognome.text()
            data = self.dateEdit.text()
            luogo = self.line_luogo_nascita.text()
            codice_fiscale = self.line_codice_fiscale.text()
            telefono = self.line_telefono.text()
            email = self.line_email.text()

            cliente = Cliente(id, nome, cognome, codice_fiscale, data, email, luogo, telefono)

            gestore_cliente = GestoreCliente()
            gestore_cliente.modifica_cliente(cliente)

            from Viste.GestioneClienti.VistaGestioneCliente import VistaGestioneCliente
            self.vista_gestione_cliente = VistaGestioneCliente(cliente)
            self.vista_gestione_cliente.show()
            self.close()
        except Exception as e:
            print(f"Errore durante la conferma: {e}")