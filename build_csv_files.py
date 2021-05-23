
from sys import argv, exit, stderr
from os import path
import csv

def room_draw_history(filename):
    # ensure file is string
    assert isinstance(filename, str), f"Input of room_draw_history is of type {type(filename)} and not of type string"
    
    #open  and read file
    with open(filename, "r") as history_text:
        table = []
        for line in history_text:
            
    #format info
            line= line.strip().strip('\n')
            space_cnt = 0
            string = ""
            char_cnt = 0
            row = {}

            for c in line:
                char_cnt += 1
                if c == " ":
                    space_cnt += 1
                
                    if space_cnt == 1:
                        row["Building"] = string
                        string = ""
    
                    elif space_cnt == 2:
                        string = ""
                    
                    elif space_cnt == 3:
                        row["Room"] = string
                        string = ""
                        remaining_characters = line[char_cnt:]
                        row["Date/Time"] = remaining_characters
                        
                else:
                    string += c 

            table.append(row)
            
    # write file to csv
    
    csv_filename = filename[:-3] + "csv"

    with open(csv_filename, newline='',mode='w') as csv_file:
        fieldnames = ["Building", "Room", "Date/Time"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in table:
            writer.writerow(row)

    print("completed " + csv_filename)


def available_rooms(filename):
    # ensure file is string
    assert isinstance(filename, str), f"Input of available_rooms is of type {type(filename)} and not of type string"
    
    #open and read file
    with open(filename, "r") as available_room_text:
        table = []
        for line in available_room_text:
            
    #format info
            space_cnt = 0
            string = ""
            char_cnt = 0
            row = {}

            for c in line:
                char_cnt += 1
                if c == " ":
                    space_cnt += 1
                
                    if space_cnt == 1:
                        row["Building"] = string
                        string = ""
    
                    elif space_cnt == 2:
                        row["Room"] = string
                        string = ""
                    
                    elif space_cnt == 3:
                        row["Type"] = string
                        string = ""

                    elif space_cnt == 4:
                        row["Size"] = string
                        string = ""

                    elif c == '\n' and space_cnt == 4 or space_cnt == 5:
                        row["Affiliation"] = string
                        string = ""
                        remaining_characters = line[char_cnt:]
                        row["Theme"] = remaining_characters
       
                else:
                    string += c 

            table.append(row)
            
    # write file to csv
    
    csv_filename = filename[:-3] + "csv"

    with open(csv_filename, newline='',mode='w') as csv_file:
        fieldnames = ["Building", "Room", "Unit", "Type", "Size", "Affiliation", "Theme"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in table:
            writer.writerow(row)

    print("completed " + csv_filename)

def main(argv):
    room_draw_history("2019_room_draw_times.txt")
    available_rooms("all_available_rooms.txt")
    

if __name__ == '__main__':
    main(argv)
