from overlap_hours import funcs
import ast

def main():
    #input should be: [{'key': 'value', 'key': 'value', 'key': 'value'}, ...] 
    days_hours = input("Enter day, start and end hours: ")
    
    #converts to dict
    data = ast.literal_eval(days_hours)
    
    funcs.overlapping_days(data)
    funcs.overlapping_time(data)
    
if __name__ == "__main__":
    main()