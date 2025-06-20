from ..funcs import overlapping

def run_overlap_funcs(data: dict) -> bool:
    #google-style documentation
    """
    Interface for better handling the two overlap functions
    
    Args:
        data(dict) -> contains input for day, start and end times
    
    Returns:
        bool:
            - True if input is valid
            - False if input is invalid
    
    """
   
    if False in overlapping(data=data):
        return False
    return True