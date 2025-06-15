import json
import os
import shutil
from datetime import datetime

class GestoreBackup:
    def __init__(self, cartellaSorgente, cartellaBackup, dataUltimoBackup, fileDataBackup):
        self.cartellaSorgente = cartellaSorgente
        self.cartellaBackup = cartellaBackup
        self.dataUltimoBackup = dataUltimoBackup
        self.fileDataBackup = fileDataBackup
        self.leggi_data_backup()

    def leggi_data_backup(self):
        if os.path.exists(self.fileDataBackup):
            with open(self.fileDataBackup, 'r') as f:
                try:
                    data = json.load(f)
                    self.dataUltimoBackup = datetime.strptime(data.get("dataUltimoBackup"), "%Y-%m-%d").date()
                except Exception as e:
                    print(f"Errore nella lettura del file di backup: {e}")
                    self.dataUltimoBackup = None
        else:
            self.dataUltimoBackup = None

    def salva_data_backup(self):
        with open(self.fileDataBackup, 'w') as f:
            data = {"dataUltimoBackup": datetime.now().strftime("%Y-%m-%d")}
            json.dump(data, f)

    def esegui_backup(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_subfolder = os.path.join(self.cartellaBackup, f"backup_{timestamp}")

        # Crea la cartella di backup se non esiste
        os.makedirs(backup_subfolder, exist_ok=True)

        # Per copiare tutti i file JSON dalla cartella di origine a quella di backup
        for filename in os.listdir(self.cartellaSorgente):
            if filename.endswith(".json"):
                file_path = os.path.join(self.cartellaSorgente, filename)
                shutil.copy(file_path, backup_subfolder)

        print(f"Backup completato: {backup_subfolder}")

        self.salva_data_backup()