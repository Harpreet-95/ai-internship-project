
from loader import load_data
from processor import process_data


def run_pipeline():
    data = load_data()
    processed = process_data(data)

    print("Pipeline output:")
    print(processed)


if __name__ == "__main__":
    run_pipeline()
