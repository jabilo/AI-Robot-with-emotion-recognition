import multiprocessing

if __name__ == '__main__':
    # Create two processes, one for each file
    p1 = multiprocessing.Process(target=exec(open("app.py").read()))
    p2 = multiprocessing.Process(target=exec(open("main.py").read()))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()
