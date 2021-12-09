import datetime
import sys
import project_modules.csv_reader as csv_reader


def start_teach_ui():  # Tämän metodin sisään kutsut algoritmin opettamiseksi
    while True:
        print("Opetetaan...")
        if input("Lopetetaanko opettaminen k/e").lower() == "k":
            break


def start_validate_ui():  # Tämän metodin sisään kutsu algoritmin validointia varten
    while True:
        print("Validoidaan...")
        if input("Lopetetaanko validointi k/e").lower() == "k":
            break


def start_use_ui():  # Tällä metodilla voidaan käyttää algoritmiä
    stations = ["asema1", "asema2", "asema3"]  # tähän tulee csv_readerillä luettu lista asemista

    station_found = False
    while not station_found:
        selected_station = input("Syötä Kaupunkipyöräaseman nimi:").lower()
        if selected_station in stations:
            station_found = True
            print(f"Kaupunkipyöräasema {selected_station} löytyi\n")
        else:
            print(f"Kaupunkipyöräasemaa {selected_station} ei löytynyt!")
    weekdays_fi = {
        1: "maanantai",
        2: "tiistai",
        3: "keskiviikko",
        4: "torstai",
        5: "perjantai",
        6: "lauantai",
        7: "sunnuntai"
    }
    print("{:<8} {:<15}".format('Avain', 'Viikonpäivä'))
    for key, weekday in weekdays_fi.items():
        print("{:<8} {:<15}".format(key, weekday))
    weekday = input("\nSyötä viikonpäivää vastaava avain:")


if __name__ == "__main__":
    print("\n!!! HSL Kaupunkipyörien asematilanne ennustaja !!!\n")
    options = {
        1: "Algoritmin opetus",
        2: "Validointi",
        3: "Käytä ohjelmaa",
        0: "Lopeta ohjelma",
    }

    while True:
        print("\n{:<8} {:<15}".format('Valinta', 'Toiminto'))
        for choice, function in options.items():
            print("{:<8} {:<15}".format(choice, function))

        selected = int(input("Valitse toiminto: "))
        if selected == 0:
            print("Ohjelma lopetetaan!")
            sys.exit(0)
        elif selected == 1:
            start_teach_ui()
        elif selected == 2:
            start_validate_ui()
        elif selected == 3:
            start_use_ui()
        else:
            print("\nValitse toiminto syöttämällä toimintoa vastaava numero!\n")

