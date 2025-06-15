import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox

from Viste.VistaHome import VistaHome

class VistaLogin(QWidget):

    def __init__(self, admin):
        super().__init__()

        self.admin = admin

        self.setWindowTitle("VideoSpace")
        self.setFixedSize(600, 600)

        font = QFont("impact", 20)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        container_logo = QLabel()
        image_path = os.path.join("src", "Logo.png")
        logo = QPixmap(image_path)

        if logo.isNull():
            print(f"ATTENZIONE: Impossibile caricare l'immagine dal percorso '{image_path}'")
            container_logo.setText("Logo non trovato")
        else:
            container_logo.setPixmap(logo.scaledToWidth(400))
            
        container_logo.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.addWidget(container_logo)

        label_login = QLabel("Login")
        label_login.setFont(font)
        label_login.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.addWidget(label_login)

        layout.addSpacing(40)

        input_layout = QVBoxLayout()
        input_layout.setAlignment(Qt.AlignHCenter)

        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Username")
        self.input_username.setFixedWidth(300)
        input_layout.addWidget(self.input_username)

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Password")
        self.input_password.setFixedWidth(300)
        self.input_password.setEchoMode(QLineEdit.Password)
        input_layout.addWidget(self.input_password)

        input_layout.addSpacing(20)

        layout_bottone = QHBoxLayout()
        layout_bottone.setAlignment(Qt.AlignHCenter)

        bottone_accedi = QPushButton("Accedi")
        bottone_accedi.setFixedWidth(100)
        layout_bottone.addWidget(bottone_accedi)

        input_layout.addLayout(layout_bottone)

        layout.addLayout(input_layout)

        bottone_accedi.clicked.connect(self.on_click_accedi)

        self.setLayout(layout)

    def on_click_accedi(self):
        username_inserito = self.input_username.text()
        password_inserita = self.input_password.text()
        if self.admin.getUsername() == username_inserito and self.admin.getPassword() == password_inserita:
            self.vista_home = VistaHome()
            self.vista_home.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Errore', 'Username o password non validi')