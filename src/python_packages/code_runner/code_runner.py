"""This module defines functions for setting up and starting the script."""

import os, time
from contextlib import contextmanager

def run_script():
    """Starts the python script."""
    
    from python_packages.prime_finder.prime_finder import find_primes
    from cython_extensions.primeFinder.primeFinder import findPrimes
    from cython_extensions.optimizedPrimeFinder.optimizedPrimeFinder import optimizedFindPrimes
    from cython_extensions.cppPrimeFinder.cppPrimeFinder import cppFindPrimes
    
    start_from, end_with = 2, 500000
    
    start = time.time()
    output1 = find_primes(start_from, end_with)
    len1 = len(output1)
    time1 = time.time() - start
    
    start = time.time()
    output2 = findPrimes(start_from, end_with)
    len2 = len(output2)
    time2 = time.time() - start
    
    start = time.time()
    output3 = optimizedFindPrimes(start_from, end_with)
    len3 = len(output3)
    time3 = time.time() - start
    
    start = time.time()
    output4 = cppFindPrimes(start_from, end_with)
    len4 = len(output4)
    time4 = time.time() - start
    
    print("Results:")
    print(f"Python     found {len1} primes and took {time1} seconds.")
    print(f"NormCython found {len2} primes and took {time2} seconds.")
    print(f"OptCython  found {len3} primes and took {time3} seconds.")
    print(f"CppCython  found {len4} primes and took {time4} seconds.")
    print("\n")
    
    print("Cross comparisons:")
    print(f"Python     vs. NormCython is {time2 / time1 : 7.3f} times faster or {time1 / time2 : 7.3f} slower.")
    print(f"Python     vs. OptCython  is {time3 / time1 : 7.3f} times faster or {time1 / time3 : 7.3f} slower.")
    print(f"Python     vs. CppCython  is {time4 / time1 : 7.3f} times faster or {time1 / time4 : 7.3f} slower.")
    print("")
    
    print(f"NormCython vs. Python     is {time1 / time2 : 7.3f} times faster or {time2 / time1 : 7.3f} slower.")
    print(f"NormCython vs. OptCython  is {time3 / time2 : 7.3f} times faster or {time2 / time3 : 7.3f} slower.")
    print(f"NormCython vs. NormCython is {time4 / time2 : 7.3f} times faster or {time2 / time4 : 7.3f} slower.")
    print("")
    
    print(f"OptCython  vs. Python     is {time1 / time3 : 7.3f} times faster or {time3 / time1 : 7.3f} slower.")
    print(f"OptCython  vs. NormCython is {time2 / time3 : 7.3f} times faster or {time3 / time2 : 7.3f} slower.")
    print(f"OptCython  vs. CppCython  is {time4 / time3 : 7.3f} times faster or {time3 / time4 : 7.3f} slower.")
    print("")
    
    print(f"CppCython  vs. Python     is {time1 / time4 : 7.3f} times faster or {time4 / time1 : 7.3f} slower.")
    print(f"CppCython  vs. NormCython is {time2 / time4 : 7.3f} times faster or {time4 / time2 : 7.3f} slower.")
    print(f"CppCython  vs. OptCython  is {time3 / time4 : 7.3f} times faster or {time4 / time3 : 7.3f} slower.")
    print("\n")
    
    print("Sorted by time:")
    for name, value in sorted((("Python", time1), ("NormCython", time2), ("OptCython", time3), ("CppCython", time4)), key=lambda x: x[1]):
        print(f"{name:10} took {value:22} seconds.")
    print("")
    
    NormCythonMissingItems = set(output1) - set(output2)
    OptCythonMissingItems   = set(output1) - set(output3)
    CppCythonMissingItems  = set(output1) - set(output4)
    
    if NormCythonMissingItems:
        print(f"Warning! The output from 'NormCython' has some missing numbers: {NormCythonMissingItems}")
    
    if OptCythonMissingItems:
        print(f"Warning! The output from 'OptCython' has some missing numbers: {OptCythonMissingItems}")
    
    if CppCythonMissingItems:
        print(f"Warning! The output from 'CppCython' has some missing numbers: {CppCythonMissingItems}")


# Source: https://dev.to/rydra/getting-started-on-profiling-with-python-3a4
# Useful: https://coderzcolumn.com/tutorials/python/yappi-yet-another-python-profiler, https://github.com/sumerc/yappi/blob/master/doc/api.md
@contextmanager
def profilerManager(filename="", engine="yappi", clock="wall", output_type="pstat", profile_builtins=True, profile_threads=True, save_near_module=False):
    """
    Description:
        A context manager that can be used to profile a block of code.
    ---
    Parameters:
        `filename -> str`
            The output file name. Defaults to the date of running this context manager `"Y-m-d (Ip-M-S).prof"`.
        
        `engine -> str`
            Selects one of the next two profilers: `yappi`, `cprofiler`.
        
        `clock -> str`
            Sets the underlying clock type (`wall` or `cpu`).
        
        `output_type -> str`
            The target type that the profile stats will be saved in. Can be either "pstat" or "callgrind".
        
        `profile_builtins -> bool`
            Enable profiling for built-in functions.
        
        `profile_threads -> bool`
            Enable profiling for all threads or just the main thread.
        
        `save_near_module -> bool`
            Selects where to save the output file. `True` will save the file relative to this module's location,
            and `False` will save it relative to the current working directory.
    ---
    Usage:
    >>> with profile():
            # Some code.
    """
    
    from datetime import datetime as dt
    
    # Making a directory to store the profiling results.
    if save_near_module:
        output_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dumpfiles")
    else:
        output_location = os.path.join(os.getcwd(), "dumpfiles")
    
    os.makedirs(output_location, exist_ok=True)
    
    if not filename:
        output_location = os.path.join(output_location, f"{dt.now().strftime('%Y-%m-%d (%I%p-%M-%S)')}.prof")
    else:
        output_location = os.path.join(output_location, filename)
    
    print("PROFILING ENABLED.")
    
    if engine == 'yappi':
        import yappi
        
        try:
            yappi.set_clock_type(clock)
            yappi.start(builtins=profile_builtins, profile_threads=profile_threads)
            
            # The yield statement is used to temporarily suspend the execution of the context manager and return control to the caller.
            # When the context manager is exited (either normally or due to an exception), the code after the yield statement is
            # executed to clean up any resources used by the context manager.
            yield
        
        finally:
            yappi.stop()
            
            print(f"Dumping profile to: {output_location}\n")
            
            yappi.get_func_stats().save(output_location, type=output_type)
            
            yappi.get_thread_stats().print_all()
    
    else:
        import cProfile
        
        profiler = cProfile.Profile()
        try:
            profiler.enable()
            yield
        
        finally:
            profiler.disable()
            profiler.print_stats()
            profiler.dump_stats(output_location)
            
            from pyprof2calltree import convert, visualize
            
            print("Saving the profiling results as `kgrind`...")
            convert(profiler.getstats(), os.path.join(os.path.splitext(output_location)[0], 'profiling_results.kgrind'))
            
            # `visualize` requires you have a separate program to work. You can download this and add it to the
            # system's path environment vairable: https://sourceforge.net/projects/qcachegrindwin/files/0.7.4/
            print("visualize the profiling results...")
            visualize(profiler.getstats())


def run_script_with_profiling(filename="", engine="yappi", clock="wall", output_type="pstat", profile_builtins=True, profile_threads=True, save_near_module=False):
    """Starts the main script with profiling."""
    
    with profilerManager(filename=filename, engine=engine, clock=clock, output_type=output_type, profile_builtins=profile_builtins, profile_threads=profile_threads, save_near_module=save_near_module):
        run_script()
