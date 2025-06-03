from ..funcs import overlapping_days, overlapping_time

def interf_run(data: dict, operation: str = 'both') -> bool:
    #google-style documentation
    """
    Interface for better handling the two overlap functions
    
    Args:
        data(dict) -> contains input for day, start and end times
        operation(str) -> which one of the two overlapping functions to call(default value is 'both')
    
    Returns:
        bool:
            - True if input is valid
            - False if input is invalid
    
    Raises:
        ValueError: if user tries to enter invalid operation
    
    """
    #new solution
    if operation != 'both':
        return False
        #first way
    if False in [overlapping_days(data=data), overlapping_time(data=data)]:
        return False
    return True

        # second way using all() -> returns true if all values are true
    # return all([
    #     overlapping_days(data=data),
    #     overlapping_time(data=data)
    # ])
    
    
    
    
    
    # try:
    #     if operation == "both":
    #         overlapping_days(data), overlapping_time(data)
    #     else:
    #         raise ValueError("Invalid operation")
        
    #     return True
    # except Exception as e:
    #     print(f"Error: {e}")
    #     return False