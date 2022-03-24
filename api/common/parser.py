import time
import json
from typing import List

def parse(input_data: List[str]) -> str:
  # check if input_data is VALID here or before calling this function
  parsed_data = {
    'time': int(time.time()), # unix time
    'id': input_data[0],
    'air_pres': input_data[1],
    'gas_res': input_data[2],
    'air_temp': input_data[3],
    'air_hum': input_data[4],
    'gnd_temp': input_data[5],
    'gnd_hum': input_data[6],
  } 
  return json.dumps(parsed_data)


def format_json(parsed_str: str) -> None:
  print(json.dumps(json.loads(parsed_str), indent=4, sort_keys=False))


if __name__ == "__main__":
  example_data = ['103', '949.00', '158.00', '23.00', '50.00', '2.00', '84.00']
  format_json(parse(example_data))
