import datetime
import sys
import project_modules.csv_reader as csv_reader
import project_modules.data_analyser as data_analyser
import project_modules.utils as utils


def start_teach_ui():  # Tämän metodin sisään kutsut algoritmin opettamiseksi
    station_data = csv_reader.get_stations().to_dict(
        'split')  # {1: "asema1", 2: "asema2", 3: "asema3"}  # tähän tulee csv_readerillä luettu lista asemista
    station_names = {}
    for data in station_data.get('data'):
        station_names[data[0]] = data[1]
    while True:
        data = csv_reader.read_data()

        for st_id, station in station_names.items():

            st_dep = utils.filter_departure_station(data, st_id)
            st_ret = utils.filter_return_station(data, st_id)
            for weekday in range(0, 7):
                data_out = {}
                data_filtered_dep = utils.filter_departure_date(st_dep, weekday)
                data_filtered_ret = utils.filter_departure_date(st_ret, weekday)
                original_stdout = sys.stdout  # Save a reference to the original standard output
                '''filename = 'Data/asemadata/' + station + '_' + str(weekday) + '.txt'
                
                with open(filename, 'w') as f:
                    sys.stdout = f  # Change the standard output to the file we created.
                    print(data_filtered)
                    sys.stdout = original_stdout  # Reset the standard output to its original value
                #data_analyser.set_data(data_filtered)
                '''
                for i_qwe in range(len(data_filtered_dep.index)):
                    data_out[i_qwe] = -1

                save_i = len(data_out)
                for i_etr in range(len(data_filtered_ret.index)):
                    data_out[i_etr+save_i] = 1
                sum_asd = 0
                for id_asd, value in data_out.items():
                    sum_asd = sum_asd + value
                    data_out[id_asd] = sum_asd
                data_analyser.set_data(data_out)
                data_analyser.split_data()
                data_analyser.train()
                print(station + ', ' + str(weekday) + ': ' + str(data_analyser.get_coef()))
        # print(data)
        data = data.get('Departure day').tolist()
        # print(data)
        # data_analyser.set_data(data)
        # data_analyser.train()
        # print(data_analyser.get_prediction_coef())

        if input("Lopetetaanko opettaminen k/e").lower() == "k":
            break


def start_validate_ui():  # Tämän metodin sisään kutsu algoritmin validointia varten
    while True:
        print("Validoidaan...")
        if input("Lopetetaanko validointi k/e").lower() == "k":
            break


def start_use_ui():  # Tällä metodilla voidaan käyttää algoritmiä
    station_data = csv_reader.get_stations().to_dict(
        'split')  # {1: "asema1", 2: "asema2", 3: "asema3"}  # tähän tulee csv_readerillä luettu lista asemista
    station_names = {}
    for data in station_data.get('data'):
        station_names[data[0]] = data[1]
    while True:
        selected_station = input(
            "Syötä Kaupunkipyöräaseman nimi (saat listan asemista kirjoittamalla \"help\"):").lower()
        if selected_station == "help":
            print("{:<10} {:<20}".format('Aseman id', 'Aseman nimi'))
            for station_id, station_name in station_names.items():
                print("{:<10} {:<20}".format(station_id, station_name))
            continue
        elif selected_station in [station.lower() for station in station_names.values()]:
            print(f"Kaupunkipyöräasema {selected_station} löytyi\n")
            break
        else:
            print(f"Kaupunkipyöräasemaa {selected_station} ei löytynyt!")
            continue

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
