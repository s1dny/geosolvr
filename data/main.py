import threading

from data import Generator, Downloader

API_KEY = 'AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg' #public google key
THREADS = 16

threads = []

for _ in range(THREADS):
    thread = threading.Thread(target = Generator, kwargs={'num_images': 20, 'output_file': 'results.csv', 'api_key': API_KEY, 'threads': THREADS})
    threads.append(thread)
    
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
    
Downloader(results_file = 'results.csv', img_directory = 'src', api_key = API_KEY)