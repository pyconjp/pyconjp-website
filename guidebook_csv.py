#:coding=utf-8:

import sys
import csv


def main(schedule_csv, presentations_csv, guidebook_csv):
    schedule_reader = csv.DictReader(open(schedule_csv))
    presentations_reader = csv.DictReader(open(presentations_csv))

    schedule_items = []
    for schedule in schedule_reader:
        for place in schedule['Room'].split(","):
            schedule_items.append({
                'Session Title': schedule['Name'],
                'Date':  schedule['Day'],
                'Time Start': schedule['Start'],
                'Time End': schedule['End'],
                'Room/Location': place,
                'Schedule Track (Optional)': place,
                'Description (Optional)': '',
            })

    for presentation in presentations_reader:
        for schedule in schedule_items:
            if schedule['Session Title'] == presentation['Name']:
                schedule['Description (Optional)'] = presentation['Description']

    writer = csv.DictWriter(open(guidebook_csv, "wb"), fieldnames=[
        'Session Title',
        'Date',
        'Time Start',
        'Time End',
        'Room/Location',
        'Schedule Track (Optional)',
        'Description (Optional)',
    ])

    writer.writeheader()
    writer.writerows(schedule_items)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
