import datetime
import project_modules.csv_reader as csv_reader

if __name__ == "__main__":
    stations = ["asema1", "asema2", "asema3"]  # tähän tulee csv_readerillä luettu lista asemista
    print("\n!!! HSL Kaupunkipyörien asematilanne ennustaja !!!\n")

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
