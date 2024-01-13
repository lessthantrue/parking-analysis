# How to use

- Install requirements with `python -m pip install -r requirements.txt`
- Go to https://openstreetmap.org
- Find the relation ID of the city you're interested in 
    - Example: "relation/198889" for Ogden, UT
- Use the `get_data` script to get geometry data for all parking spots
    - Example: `python get_data.py relation/198889 ./parking_geometry/ogden_ut`
- Open the notebook, set the values for data directory and city center boundaries, and run
