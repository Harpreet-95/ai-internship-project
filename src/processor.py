def process_data(data):
    print("Processing data...")

    processed = []

    for item in data:
        new_value = item["value"] * 2
        processed.append({"id": item["id"], "value": new_value})

    return processed