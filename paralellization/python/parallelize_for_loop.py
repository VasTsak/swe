import multiprocessing as mp
import numpy as np
import timeit

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()

# Number of processors we can utilize
print("Number of processors: ", mp.cpu_count())

# A synchronous execution is one the processes are completed 
# in the same order in which it was started. This is achieved 
# by locking the main program until the respective processes 
# are finished.

# Asynchronous, on the other hand, doesn’t involve locking. 
# As a result, the order of results can get mixed up but 
# usually gets done quicker.

# Solution Without Paralleization

def howmany_within_range(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` 
    and `minimum` in a given `row`"""
    
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    
    

    return count

# Redefine, with only 1 mandatory argument.
def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

def main():
        
    results = []
    start = timeit.default_timer()
    for row in data:
        results.append(howmany_within_range(row, minimum=4, maximum=8))
    end = timeit.default_timer()
    duration = str(end-start)
    print(f"It took: {duration} seconds without parallelization.")
    
    ### map parallelization with apply

    start = timeit.default_timer()
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # Step 2: `pool.apply` the `howmany_within_range()`
    results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]

    # Step 3: Don't forget to close
    pool.close()
    print(f"It took: {duration} seconds with apply parallelization.")


    ### map parallelization with map
    start = timeit.default_timer()
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # Step 2: `pool.apply` the `howmany_within_range()`
    results = pool.map(howmany_within_range_rowonly, [row for row in data])

    # Step 3: Don't forget to close
    pool.close()

    end = timeit.default_timer()
    duration = str(end-start)
    print(f"It took: {duration} seconds with map parallelization.")

if __name__ == "__main__":
    main()