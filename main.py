from datetime import datetime, date, timedelta, time
from PyQt5.QtWidgets import QApplication
import time as time_module
import os
import sys
import threading  # Per eseguire operazioni in parallelo

from Classi.Amministratore import Amministratore
from Classi.Mora import Mora
from Gestori.GestoreBackup import GestoreBackup
from Gestori.GestoreMora import GestoreMora
from Gestori.GestoreNoleggio import GestoreNoleggio
from Viste.VistaLogin import VistaLogin

executed = False  # Variabile per assicurarsi che l'operazione di assegnazione delle more venga eseguita una sola volta

def assegna_more():
    global executed
    data_odierna = datetime.now().strftime("%d-%m-%Y")

    try:
        if not executed:
            gestore_noleggi = GestoreNoleggio()
            gestore_mora = GestoreMora()

            lista_noleggi = gestore_noleggi.listaNoleggi
            for n in lista_noleggi:
                data_fine_str = n.getDataFine()
                data_fine = datetime.strptime(data_fine_str, "%d-%m-%Y").date()

                id_noleggio = n.getId()

                # Verifica il confronto per il primo giorno di ritardo
                if data_fine == (date.today() - timedelta(days=1)) and not n.restituito:

                    # Verifica se c'è già una mora per questo noleggio
                    mora_esiste = False
                    for m in gestore_mora.listaMore:
                        if m.idNoleggio == id_noleggio:
                            mora_esiste = True
                            break

                    if not mora_esiste:  # Se non esiste una mora, la creo
                        mora = Mora(None, data_odierna, 5, id_noleggio)
                        gestore_mora.aggiungi_mora(mora)

                elif data_fine < date.today() and not n.restituito:

                    data_inizio_str = n.dataInizio
                    data_inizio = datetime.strptime(data_inizio_str, "%d-%m-%Y").date()

                    for m in gestore_mora.listaMore:
                        if m.idNoleggio == id_noleggio and m.dataEmissioneUltima != data_odierna:

                            # Calcola la differenza tra `data_fine` e `data_inizio`
                            differenza = data_fine - data_inizio
                            giorni = differenza.days
                            prezzo_noleggio_prodotto = n.importo / giorni

                            m.importo += float((prezzo_noleggio_prodotto * 30) / 100)
                            m.dataEmissioneUltima = datetime.today().strftime("%d-%m-%Y")

                            # Modifica la mora nel file JSON
                            gestore_mora.modifica_mora(m)

            executed = True  # Per non ripetere l'esecuzione
    except Exception as e:
        print(f"Problema nel main: {e}")

def attendi_orario(ora_target, gestore_backup):
    while True:
        ora_corrente = datetime.now().time()
        data_corrente = datetime.now().date()

        # Verifica se l'orario è dopo l'ora_target e se non è stato eseguito il backup oggi
        if ora_corrente >= ora_target and data_corrente != gestore_backup.dataUltimoBackup:
            gestore_backup.esegui_backup()
            gestore_backup.dataUltimoBackup = data_corrente

            print("Backup completato.")
            time_module.sleep(24 * 60 * 60)  # Aspetta 24 ore prima di ricontrollare
        else:
            # Aspetta 60 secondi prima di controllare di nuovo
            time_module.sleep(60)


def esegui_backup_giornaliero(source_folder, backup_folder, dataUltimoBackup):
    gestore_backup = GestoreBackup(source_folder, backup_folder, dataUltimoBackup)

    ora_target = time(22, 0, 0)

    attendi_orario(ora_target, gestore_backup)

if __name__ == '__main__':
    # Admin
    admin = Amministratore(0, "Admin", "AdminAdmin", "admin", "admin1234")

    app = QApplication(sys.argv)
    main_window = VistaLogin(admin)
    app.setStyle("Fusion")
    main_window.show()

    # More
    assegna_more()

    # Backup

    # Ottiene la directory dove si trova l'eseguibile o il file Python
    base_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)

    # Percorsi relativi per backup
    source_folder = os.path.join(base_dir)
    backup_folder = os.path.join(base_dir, "Backup")
    file_data_backup = os.path.join(backup_folder, "data_backup.json")

    # Crea le cartelle se non esistono
    os.makedirs(backup_folder, exist_ok=True)

    # Crea il gestore del backup
    gestore_backup = GestoreBackup(source_folder, backup_folder, None, file_data_backup)

    # Esecuzione del backup in un thread separato
    thread_backup = threading.Thread(target=attendi_orario, args=(time(22, 0, 0), gestore_backup))
    thread_backup.daemon = True  # Fa in modo che il thread si chiude quando l'app termina
    thread_backup.start()

    # Esegue l'app Qt
    exit_code = app.exec_()
    sys.exit(exit_code)