# GeoSolvr

Machine learning model to predict location of GeoGuessr images

# Setup 
## Collecting Data
- Rename the file `data/example.csv` to `data/results.csv`
- Create a folder in the `/data` directory called `src`
- The `/data` directory should now look similar to this:  
    ```
    /data
        |-- src
        |-- .gitignore
        |-- results.csv
        |-- iso_codes.json
        |-- data.py
        |-- main.py
    ```
- Adjust the parameters in the `/data/main.py` file
- cd into the data directory and run `main.py`