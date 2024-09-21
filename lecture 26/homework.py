import time
import threading

waiting_line = [f"person_{i}" for i in range(1, 16)]


semaphore = threading.Semaphore(5)

def sell_tickets(person):
    semaphore.acquire()
    print(f"{person} is buying a ticket")
    time.sleep(5)
    print(f"{person} has bought a ticket")
    semaphore.release()

threads_lst = [threading.Thread(target=sell_tickets, args=(i, )) for i in waiting_line]

start_time = time.perf_counter()

for thread in threads_lst:
    thread.start()

for thread in threads_lst:
    thread.join()

end_time = time.perf_counter()
delta = end_time - start_time
print(f"All Tickets Were Sold in {delta} secends")







