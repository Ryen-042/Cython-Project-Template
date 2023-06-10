"""The entry point for the entire package."""
import sys, os, winsound

def main():
    """Starts the python script by calling either the `run_script` or `run_script_with_profiling` function of the code_runner module."""
    
    # Changing the working directory to where this script is.
    os.chdir(os.path.dirname(__file__))
    
    # This line adds the directory path of this module to the sys.path list.
    # sys.path is a list of strings that specifies where to search for Python modules.
    sys.path.append(os.path.dirname(__file__))
    
    if len(sys.argv) > 1 and sys.argv[1] in ("-p", "--profile", "--prof"):
        from python_packages.code_runner.code_runner import run_script_with_profiling
        
        run_script_with_profiling()
    
    else:
        from python_packages.code_runner.code_runner import run_script
        
        run_script()

if __name__ == '__main__':
    main()
    
    winsound.PlaySound(os.path.join(os.path.dirname(__file__), "SFX", "jobs_done.wav"), winsound.SND_FILENAME)
