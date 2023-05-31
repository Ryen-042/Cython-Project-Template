"""The entry point for the entire package."""
import sys, os, time, winsound

def main():
    """Starts the script by calling the `begin_script()` function from the `scriptRunner` extension module."""
    
    # Changing the working directory to where this script is.
    os.chdir(os.path.dirname(__file__))
    
    # This line adds the directory path of this module to the sys.path list.
    # sys.path is a list of strings that specifies the search path for Python modules.
    # By adding the directory path of the script file to this list, it allows Python to
    # locate and import any modules in that directory as well as any subdirectories within it.
    sys.path.append(os.path.dirname(__file__))
    
    from extensions.primeFinder.primeFinder import prime_finder
    from extensions.optimizedPrimeFinder.optimizedPrimeFinder import optimized_prime_finder
    
    start = time.time()
    len1 = len(prime_finder(0, 10_000))
    time1 = time.time() - start
    print(f"Found primes are: {len1}. Took {time1} seconds.")
    
    start = time.time()
    len2 = len(optimized_prime_finder(0, 10_000))
    time2 = time.time() - start
    print(f"Found primes are: {len2}. Took {time2} seconds.")
    
    print(f"Optimized version is {time1 / time2} times faster than the original version.")

if __name__ == '__main__':
    main()
    
    winsound.PlaySound(os.path.join(os.path.dirname(__file__), "SFX", "jobs_done.wav"), winsound.SND_FILENAME)
