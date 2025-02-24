# python3 ordinary.py ratings.csv
import os
import sys
import resource

def file_reader(input_file):
    with open(input_file, 'r') as fils:
        return fils.readlines()


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python3 ordinary.py <input_file>")\
        
        file_path = sys.argv[1]

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        start_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime

        lines = file_reader(file_path)
        for line in lines:
            pass
        
        end_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime
        peak_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        peak_mem_usage = peak_mem / (1024 * 1024)
        elapsed_time = end_time - start_time

        print(f"Peak Memory Usage = {peak_mem_usage:.3f} GB")
        print(f"User Mode Time + System Moode Time = {elapsed_time:.3f}s")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    