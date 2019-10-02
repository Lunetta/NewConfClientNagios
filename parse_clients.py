import json
import argparse


def generate_json(clients_file):
    with open(clients_file, 'r') as f:
        lines = f.readlines()

    lines = lines[1:]
    clients = {}
    for line in lines:
        company, city, address = line.split("\t")
        clients[company + "-" + city.split(" -")[0]] = address.rstrip()

    with open(clients_file.rstrip("txt") + "json", 'w') as f:
        json.dump(clients, f, indent=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("clients_file", type=str, help="clients specification file path")
    args = parser.parse_args()

    generate_json(args.clients_file)
