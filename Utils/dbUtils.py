import json


def load_json(db_path):
    with open(f'{db_path}', 'r') as f:
        db = json.load(f)
    return db


def save_json(db, db_path):
    with open(f'{db_path}', 'w') as f:
        json.dump(db, f)
    return db


def get_values(db, col):
    return list(set([user[col] for user in db]))


def filter_db(db, feature):
    cols = list(feature.keys())
    values = list(feature.values())

    users = db

    for i in range(0, len(values)):
        if values[i] != "":
            users = [user for user in users if user[cols[i]] == values[i]]

    return users


def find_idx(db, feature):
    # found = 0
    idx = None
    # found_idx=None



    range_db=range(len(db))
    range_feature=(range(len(feature)))

    cols = list(feature.keys())
    values = list(feature.values())


    for i in range_db:
        found = 0
        for j in range_feature:
            if db[i][cols[j]] == values[j]:
                # found_idx=i
                found+=1
                if found == len(values):
                    idx=i
                    return idx
    return idx
