# python3

def parallel_processing(n, m, data):
    output = []
    # Initialize a list to store the finish time of each thread
    finish_time = [0] * n

    # Create a list of threads and initialize them with their indexes
    threads = list(range(n))

    # Iterate over the jobs
    for i in range(m):
        # Find the next available thread
        next_thread = min(threads, key=lambda x: finish_time[x])

        # Calculate the start time of the current job for the selected thread
        start_time = finish_time[next_thread]

        # Calculate the finish time of the current job for the selected thread
        finish_time[next_thread] = start_time + data[i]

        # Append the output pair (thread index, start time) to the output list
        output.append((next_thread, start_time))

    return output


def main():
    # Read input from keyboard
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # Call the parallel_processing function
    result = parallel_processing(n, m, data)

    # Print out the results
    for thread_index, start_time in result:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()