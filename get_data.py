from OSMPythonTools.overpass import Overpass, overpassQueryBuilder
from OSMPythonTools.api import Api
import json

def get_parking_data(area):
    query = overpassQueryBuilder(
        area=area, 
        selector='"amenity"="parking"', 
        elementType="way"
    )

    overpass = Overpass()
    lots = overpass.query(query)

    return lots

def save_data(data_dir, query_result):
    for w in query_result.ways():
        file_path = os.path.join(data_dir, f"way-{w.id()}.json")
        with open(file_path, "wt") as f:
            json.dump(w.geometry(), f)

if __name__ == "__main__":
    import argparse
    import os
    import shutil

    parser = argparse.ArgumentParser()

    parser.add_argument("osm_area_name")
    parser.add_argument("data_folder")
    parser.add_argument("--replace", action="store_true")

    args = parser.parse_args()

    parking_lot_data = get_parking_data(args.osm_area_name)

    if args.replace and os.path.exists(args.data_folder):
        shutil.rmtree(args.data_folder)
    os.makedirs(args.data_folder)

    save_data(args.data_folder, parking_lot_data)
