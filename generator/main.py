import threading

from data import Generator, Downloader

API_KEY = 'AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg' #public google key
THREADS = 8

threads = []

for _ in range(THREADS):
    thread = threading.Thread(target=Generator, args=(4, 'results.csv', API_KEY, THREADS))
    threads.append(thread)
    
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

Downloader('results.csv', 'src', API_KEY)