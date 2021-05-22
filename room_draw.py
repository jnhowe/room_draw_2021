
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

#Cuyler Hall 322 5/6/19 11:43 AM
#Cuyler Hall 402 5/6/19 11:44 AM            
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



    # end function



def main(argv):
    room_draw_history('2019_room_draw_times.txt')
    

if __name__ == '__main__':
    main(argv)
