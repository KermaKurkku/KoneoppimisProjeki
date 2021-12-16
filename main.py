import datetime
import sys
import project_modules.csv_reader as csv_reader
import project_modules.data_analyser as data_analyser
import project_modules.utils as utils
import collections
import warnings


def start_teach_ui():  # Tämän metodin sisään kutsut algoritmin opettamiseksi
    station_data = csv_reader.get_stations().to_dict(
        'split')  # tähän tulee csv_readerillä luettu lista asemista
    station_names = {}
    for data in station_data.get('data'):
        station_names[data[0]] = data[1]

    while True:
        if input("\nHaluatko luoda uuden mallin? k/e").lower() != "k":
            break
        data = csv_reader.read_data()
        asema = 0
        for st_id, station in station_names.items():
            asema += 1
            sys.stdout.write("\rMallista valmiina %.2f%%" % ((asema / len(station_names)) * 100))
            sys.stdout.flush()
            # print('Valmistellaan dataa asemalle ' + station + '... ', end='')
            st_dep = utils.filter_departure_station(data, st_id)
            st_ret = utils.filter_return_station(data, st_id)
            if st_dep.empty:
                continue
            if st_ret.empty:
                continue
            st_dep.sort_values('Departure')
            st_ret.sort_values('Return')

            data_out = {}

            for dep_i, dep_row in st_dep.iterrows():
                if dep_row['Departure'] not in data_out:
                    data_out[dep_row['Departure']] = -1
                else:
                    data_out[dep_row['Departure']] -= 1

            for ret_i, ret_row in st_ret.iterrows():
                if ret_row['Return'] not in data_out:
                    data_out[ret_row['Return']] = 1
                else:
                    data_out[ret_row['Return']] += 1
            data_out2 = {}
            for do_key, do_value in data_out.items():
                data_out2[str(do_key)] = do_value

            #ordered_data = dict(sorted(data_out2.items()))
            data_analyser.set_data(data_out2)
            data_analyser.split_data()
            data_analyser.train()
            data_analyser.predict()
            data_analyser.plot_outputs(station)
            data_analyser.save_model(str(st_id))


def start_validate_ui():
    while True:
        print("Validoidaan...")
        station_data = csv_reader.get_stations().to_dict('split')
        station_names = {}
        for data in station_data.get('data'):
            station_names[data[0]] = data[1]
        score_sum = 0
        score_max = -100.0
        score_min = 100.0
        validated_num = 0
        for st_id, station in station_names.items():
            print("Validoidaan asema", station, ": ", end="")
            if data_analyser.load_model(str(st_id)) == -1:
                continue
            validate_result = data_analyser.validate_model()
            print("Score:", round(validate_result['score'], 4),
                  "Crossval:", validate_result['cross val score'], "\n")
            if validate_result['score'] < score_min:
                score_min = validate_result['score']
            if validate_result['score'] > score_max:
                score_max = validate_result['score']

            score_sum += validate_result['score']
            validated_num += 1
        print("\nScore MIN:", round(score_min, 2))
        print("\nScore MAX:", round(score_max, 2))
        print("\nScore KA:", round((score_sum / validated_num), 2))
        if input("Lopetetaanko validointi k/e").lower() == "k":
            break


def start_use_ui():  # Tällä metodilla voidaan käyttää algoritmiä
    station_data = csv_reader.get_stations().to_dict('split')
    station_names = {}
    for data in station_data.get('data'):
        station_names[data[1].lower()] = data[0]
    while True:
        selected_station = input(
            "Syötä Kaupunkipyöräaseman nimi (saat listan asemista kirjoittamalla \"help\"):").lower()
        if selected_station == "help":
            print("{:<30} {:<10}".format('Aseman nimi', 'Aseman id'))
            for station_id, station_name in station_names.items():
                print("{:<30} {:<10}".format(station_id, station_name))
            continue
        elif selected_station in [station.lower() for station in station_names.keys()]:
            print(f"Kaupunkipyöräasema {selected_station} löytyi\n")
            break
        else:
            print(f"Kaupunkipyöräasemaa {selected_station} ei löytynyt!")
            continue

    weekdays_fi = {
        0: "maanantai",
        1: "tiistai",
        2: "keskiviikko",
        3: "torstai",
        4: "perjantai",
        5: "lauantai",
        6: "sunnuntai"
    }
    print("{:<8} {:<15}".format('Avain', 'Viikonpäivä'))
    for key, weekday in weekdays_fi.items():
        print("{:<8} {:<15}".format(key, weekday))
    while True:
        weekday_key = input("\nSyötä viikonpäivää vastaava avain (Lopeta syöttämällä -1):")
        if weekday_key == '-1':
            break
        data_analyser.load_model(str(station_names[selected_station]))

        day = []
        for x in range(24):
            if x < 10:

                day.append([str(int(weekday_key) + x / 10)])
            else:
                day.append([str(int(weekday_key) + x / 100)])
        day = [[str(int(weekday_key)+x/100)] for x in range(24)]
        prev = 0
        for i, e in enumerate(data_analyser.do_predict(day)):
            print('Ennustus klo', i, ':', int(e))
        if input("Lopetetaanko ennustus k/e").lower() == "k":
            break


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
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
