import threading

from data import Generator, Downloader

API_KEY = 'AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg' #public google key
THREADS_GENERATOR = 16
THREADS_DOWNLOADER = 8

threads_generator = []
threads_downloader = []

for _ in range(THREADS_GENERATOR):
    thread = threading.Thread(target = Generator, kwargs={'num_images': 32, 'output_file': 'results.csv', 'api_key': API_KEY, 'threads': THREADS_GENERATOR})
    threads_generator.append(thread)
    
for thread in threads_generator:
    thread.start()

for thread in threads_generator:
    thread.join()


for thread in range(THREADS_DOWNLOADER):
    thread = threading.Thread(target = Downloader, kwargs={'results_file': 'results.csv', 'img_directory': 'src', 'api_key': API_KEY, 'threads': THREADS_DOWNLOADER, 'thread_number': thread})
    threads_downloader.append(thread)
    
for thread in threads_downloader:
    thread.start()

for thread in threads_downloader:
    thread.join()