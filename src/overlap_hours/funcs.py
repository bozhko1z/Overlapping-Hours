from collections import Counter
import logger.log_config as log
import logging

def overlapping_days(data):
    #count how many times each day appears
    #it collects all day values from all entries in data
    day_counter = Counter(day for entry in data for day in entry["Day"])

    for day, count in day_counter.items():
        #if any day appears more than once it returns false
        if count > 1:
            logging.info(f"Duplicate entries found for {day}: {count} times.")
            return False
        else:
            logging.info("No overlap")
            return True


def overlapping_time(data):
    #sorts all the items by their Start value
    data.sort(key=lambda x: x['Start'])

    # checks for any overlaps
    for i in range(len(data) - 1):
        if data[i]['End'] > data[i + 1]['Start'] and data[i]['Day'] == data[i + 1]['Day']:
            logging.error("Overlap")
            return False
        else:
            logging.info("No overlap")
            return True
