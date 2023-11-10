def format_data(data):
    return [{"id": row[0], "name": row[1]} for row in data]


def sort_data(all_data):
    return sorted(all_data, key=lambda x: x["id"])
