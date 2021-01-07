import glob
import json
import time
import pandas as pd

import pandas

data = []


def message():
    # message files in data are out of order

    # Get all files in the directory
    for file in glob.iglob(r'/Users/LinjiaTheNinja/Downloads/messages/inbox'
                           '/circusfreaks/*.json'):
        data.append(file)

    data.sort()


def graph():

    # df = pd.DataFrame({'sender_name': [], 'time': []})

    # key: name, value: time
    sender = {'Linjia Zhou': [], 'Evan Chow': [], 'Jennifer Lim': []}
    keyword = 'roach'

    for file in data:
        json_file = json.load(file)  # message_1 file

        for index in json_file["messages"]:
            word = json_file["messages"][index]["content"]
            date = time.ctime(json_file["messages"][index]["timestamp_ms"])
            name = json_file["messages"][index]["sender_name"]

            if name.equals('Jisoo Lim') or name.equals('Tara Anderson'):
                name = 'Jennifer Lim'

            if word.equals(keyword):
                # df["sender_name"].append(name)
                sender[name].append(date)


