from overlap_hours.API.overlap_checker import interf_run
import ast

def main():
    #input should be: [{'key': 'value', 'key': 'value', 'key': 'value'}, ...] 
    days_hours = input("Enter day, start and end hours: ")
    
    #converts to dict
    data = ast.literal_eval(days_hours)
    
    result = interf_run(data, "both")
    print(result)
    
if __name__ == "__main__":
    main()