from ..funcs import overlapping


def run_overlap_funcs(data: dict) -> bool:
    # google-style documentation
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

    if False in overlapping(data=data):
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
