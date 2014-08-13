#:coding=utf-8:

import zipfile

import sys
import csv


def export_schedule_csv(schedule_csv, presentations_csv, guidebook_csv):
    """
    Generate the schedule CSV
    """
    schedule_reader = csv.DictReader(schedule_csv)
    presentations_reader = csv.DictReader(presentations_csv)

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

    writer = csv.DictWriter(guidebook_csv, fieldnames=[
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


def export_speakers_csv(speakers_csv, guidebook_csv):
    speakers_reader = csv.DictReader(speakers_csv)

    writer = csv.DictWriter(guidebook_csv, fieldnames=[
        "Name",
        "Sub-Title (i.e. Location, Table/Booth, or Title/Sponsorship Level)",
        "Description (Optional)",
        "Location/Room",
        "Image (Optional)",
    ])

    writer.writeheader()

    for speaker in speakers_reader:
        writer.writerow({
            "Name": speaker['Name'],
            "Sub-Title (i.e. Location, Table/Booth, or Title/Sponsorship Level)": "",
            "Description (Optional)": speaker['Biography'],
            "Location/Room": "",
            "Image (Optional)": "",  # TODO
        })


SCHEDULE_CSV_PATH = "program_export/schedule/csv/talks_schedule.csv"
SPEAKERS_CSV_PATH = "program_export/speakers/bios/csv/all.csv"
PRESENTATIONS_CSV_PATH = u"program_export/presentations/csv/talk_session___トークセッションs.csv".encode("utf-8")

if __name__ == '__main__':

    if len(sys.argv) > 1:
        if sys.argv[1] == "create":
            program_export = zipfile.ZipFile(sys.argv[2])

            schedule_csv = program_export.open(SCHEDULE_CSV_PATH)
            presentations_csv = program_export.open(PRESENTATIONS_CSV_PATH)
            speakers_csv = program_export.open(SPEAKERS_CSV_PATH)

            export_schedule_csv(schedule_csv, presentations_csv, open("guidebook_schedule.csv", "wb"))
            export_speakers_csv(speakers_csv, open("guidebook_speakers.csv", "wb"))
        elif sys.argv[1] == "links":
            print("Not yet supported...")
        else:
            print("Unknown command: %s" % sys.argv[1])
    else:
        print("%s - Guidebook Data Script." % sys.argv[0])
        print("")
        print("%s create PROGRAM_EXPORT_ZIP" % sys.argv[0])
        print("Output data to guidebook_schedule.csv, guidebook_speakers.csv")
        # TODO
        #print("")
        #print("%s links PROGRAM_EXPORT_ZIP SESSION_EXPORT_CSV SPEAKERS_EXPORT_CSV" % sys.argv[0])
        #print("Output session/speaker link data to guidebook_session_links.csv")
