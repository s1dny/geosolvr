import requests
import json
import random
import wget
import csv
import os
import pandas as pd

results = pd.read_csv('results.csv')

try:
    df_results = pd.DataFrame(results.iloc[-1:,:].values, index=None)
    index = int(list(df_results[0])[0].split('.')[0])

except:
    index = 0

global_image_num = 0


class Colors:
    BOLD = '\033[1m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

class Generator:
    def __init__(self, num_images, output_file, api_key, threads):
        self.num_images = num_images
        self.output_file = output_file
        self.api_key = api_key
        self.threads = threads

        # gets last index of a csv file
        

        global global_image_num

        global index

        epoch = 0

        while epoch < num_images:
            coordinates = self.random_coordinates()
            metadata = self.check_streetview(coordinates[0], coordinates[1])

            if metadata != False:
                lat = metadata['location']['lat']
                lng = metadata['location']['lng']

                iso_code = self.reverse_geocode(lat, lng)

                print (f'{Colors.SUCCESS} progress [{round(((global_image_num) / (num_images * threads)) * 100, 1)}%]{Colors.END} streetview found in {iso_code}\n{lat},{lng}')
                
                global_image_num += 1

                index += 1

                with open(output_file, 'a') as f:
                    f.write(f'{str(index).zfill(6)}.png,{iso_code},{lat},{lng},{random.randint(0, 359)}\n')
                
                epoch += 1

    # returns random coordinats -> List[float, float]  
    def random_coordinates(self):
        lat = random.uniform(90, -90)
        lng = random.uniform(180, -180)

        return [lat, lng]

    # checks if streetview exists -> Dict or False
    def check_streetview(self, lat, lng):
        metadata = requests.get(f'https://maps.googleapis.com/maps/api/streetview/metadata?size=640x640&location={lat},{lng}&radius=4096&key={self.api_key}').text
        metadata = json.loads(metadata)

        if metadata['status'] == 'OK' and metadata['copyright'] == '© Google':
            return metadata

        return False
    
    # converts latitude and longitude to iso code -> String
    def reverse_geocode(self, lat, lng):
        iso_code = requests.get(f'https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lng}&zoom=18&addressdetails=1')
        iso_code = iso_code.json()
        
        return iso_code['address']['country_code']

class Downloader:
    def __init__(self, results_file, img_directory, api_key, threads, thread_number):
        self.results_file = results_file
        self.img_directory = img_directory
        self.api_key = api_key
        self.threads = threads
        self.thread_number = thread_number


        # gets last index from the image directory

        try:
            file_names = os.listdir(img_directory)
            img_index = int(os.path.splitext(file_names[-1])[0])
        except:
            img_index = 0

        rows = []

        with open(results_file, 'r') as file:
            results = csv.reader(file)
            for row in results:
                rows.append(row)

        for i in range(img_index + 1, len(rows), threads):
            thread_index = i + thread_number
            try:
                lat = rows[thread_index][2]
                lng = rows[thread_index][3]
                heading = rows[thread_index][4]

                wget.download(f'https://maps.googleapis.com/maps/api/streetview?size=640x640&location={lat},{lng}&fov=180&heading={heading}&pitch=0&key={api_key}', out=f'{self.img_directory}/{str(thread_index).zfill(6)}.png')
            
            except Exception as e:
                ('thread index out of range: ', e)