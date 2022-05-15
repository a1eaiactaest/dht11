import time
import json
from typing import List, Iterable


def parse_to_dict(input_data: List[str]) -> str:
    # check if input_data is VALID here or before calling this function
    parsed_data = {
        "time": input_data[0],
        "id": input_data[1],
        "air_pres": input_data[2],
        "voc": input_data[3],  # it's volatile organic compound
        "air_temp": input_data[4],
        "air_hum": input_data[5],
        "gnd_temp": input_data[6],
        "gnd_hum": input_data[7],
    }
    return parsed_data

# [(3,), (5,), (11,), (103,)]


def parse_stations(input_data: List[tuple]) -> tuple:
    ret = []
    for station in input_data:
        ret.append(station[0])
    return str(ret)


def parse_to_list(input_data: List[str]) -> List[str]:
    parsed_data = [str(int(time.time()))] + input_data
    return parsed_data


def pretty_json(parsed_str: str) -> None:
    print(json.dumps(json.loads(parsed_str), indent=4, sort_keys=False))


def pretty_db_dump(dump: List[tuple]) -> None:
    # debug and developement use recommended
    for subd in dump:
        print(subd)
        pretty_json(parse_to_dict(subd))


if __name__ == "__main__":
    example_data = ['103', '949.00', '158.00',
                    '23.00', '50.00', '2.00', '84.00']
    pretty_json(parse(example_data))
