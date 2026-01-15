"""
A decorator is a way to add extra behavior to a function without changing
the function's original code.

Think of it like this:
- You already have a function that does something useful.
- You want to automatically add extra steps before and/or after it runs
  (for example: timing it, logging it, checking permissions).
- A decorator is a wrapper that sits around the function and does that extra work.

In this file:
- `mission_timer` is a decorator.
- It wraps other functions to:
  1) Print a countdown before the function runs
  2) Measure how long the function takes to execute
"""

import time  # Provides access to time-related functions like sleep() and time()


def mission_timer(base_func):
    """
    This is a DECORATOR.

    It takes another function (`base_func`) as input,
    wraps it with additional behavior, and returns a new enhanced function.
    """

    def enhanced_func(*args, **kwargs):
        """
        This inner function replaces the original function.

        *args  -> packs ALL positional arguments into a tuple
        **kwargs -> packs ALL keyword (named) arguments into a dictionary
        so it can decorate many different functions safely.
        """

        # Record the time just before the original function runs
        start_time = time.time()

        # Countdown before executing the mission
        for i in range(3, 0, -1):
            print(f"{i}...")
        '''
         Call the original function and store its return value
         base_func(*args, **kwargs) does the OPPOSITE of packing.
        
         It takes:
           args   -> tuple
           kwargs -> dictionary
        
         And EXPANDS them back into normal arguments.
        
         Example:
           args = ("polar", 800)
           kwargs = {}
        
         Becomes:
           base_func("polar", 800)
        
         This is how the original function receives
         exactly what it expects.
         -------------------------------------------------------
        '''
        result = base_func(*args, **kwargs)

        # Record the time after the function finishes
        end_time = time.time()

        # Print how long the mission took
        print(f"Misson duration: {end_time - start_time} seconds")

        # Return whatever the original function returned
        return result

    # Return the wrapped version of the function
    return enhanced_func


@mission_timer
def launch_probe(target):
    """
    Launches a probe toward a target destination.
    The decorator automatically adds timing and countdown behavior.
    """
    print(f"Launching probe toward {target}...")
    time.sleep(1)  # Simulates a 1-second launch process
    return f"Probe successfully en route to {target}."


@mission_timer
def deploy_satellite(orbit_type, altitude_km):
    """
    Deploys a satellite into a specific orbit.
    This function does NOT return anything.
    """
    print(f"Deploying satellite into {orbit_type} orbit at {altitude_km} km...")
    time.sleep(2)  # Simulates a longer deployment process


# Call the decorated function (countdown + timing happen automatically)
deploy_satellite("polar", 800)

# Call another decorated function and capture its return value
result = launch_probe("Europa")

# Print the returned result from launch_probe
print("Stored mission result:", result)
