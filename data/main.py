import threading

from data import Generate, Download, Validate

API_KEY = 'AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg' #public google key
THREADS_GENERATE = 16
THREADS_DOWNLOAD = 32

threads_generator = []
threads_downloader = []

for _ in range(THREADS_GENERATE):
    thread = threading.Thread(target = Generate, kwargs = {'num_images': 32, 'output_file': 'results.csv', 'api_key': API_KEY, 'threads': THREADS_GENERATE})
    threads_generator.append(thread)
    
for thread in threads_generator:
    thread.start()

for thread in threads_generator:
    thread.join()

Validate(input_file = 'results.csv', iso_codes_file = 'iso_codes.csv')

for thread in range(THREADS_DOWNLOAD):
    thread = threading.Thread(target = Download, kwargs = {'download_pano': True, 'results_file': 'results.csv', 'img_directory': 'src', 'api_key': API_KEY, 'threads': THREADS_DOWNLOAD, 'thread_number': thread})
    threads_downloader.append(thread)
    
for thread in threads_downloader:
    thread.start()

for thread in threads_downloader:
    thread.join()