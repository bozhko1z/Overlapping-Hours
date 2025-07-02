from overlap_app.overlap_hours.API.overlap_checker import run_overlap_funcs
import logging
import ast

def main():
    
    #input should be: [{'key': 'value', 'key': 'value', 'key': 'value'}, ...]
    logging.info("Enter day, start and end hours: ")
    days_hours = input()
    
    #converts to dict
    data = ast.literal_eval(days_hours)
    
    result = run_overlap_funcs(data)
    logging.info(result)
    
if __name__ == "__main__":
    main()