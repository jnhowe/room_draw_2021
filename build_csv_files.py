
from sys import argv, exit, stderr
from os import path
import csv


#format info in line
def format_line(line):
    #961216103 5/25/2021 9:00 10046 Cho Christine 2022
    #920209092 5/25/2021 9:00 10046 Chen Rachel 2022
    line = line.strip()
    space_cnt = 0
    string = ""
    char_cnt = 0
    row = {}
    for c in line: 
        char_cnt += 1
        if c == " ":
            space_cnt += 1
                    
            if space_cnt == 1:
                row["NetID"] = string
                string = ""

            elif space_cnt == 3:
                row["Date/Time"] = string
                string = ""

            elif space_cnt ==4 :
                string = ""

            elif space_cnt ==5 :
                string += " "

            elif space_cnt == 6:
                row["Name"] = string
                string = ""
                remaining_characters = line[char_cnt:]
                row["Class"] = remaining_characters
                
        else:
            string += c

    return row



#create csv file using a dictonary representation of data
def create_csv(filename, table):
    csv_filename = filename[:-3] + "csv"

    with open(csv_filename, newline='',mode='w') as csv_file:
        fieldnames = ["NetID", "Date/Time", "Name", "Class"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in table:
            writer.writerow(row)

    print("completed " + csv_filename)



def build_csv_file(filename):
    #ensure file is string
    assert isinstance(filename,str), f"Input of add_room_draw is of type {type(filename)} and not of type string"

    #open and read file
    with open(filename, "r") as room_draw_text:
        table = []
        for line in room_draw_text:
    
            #format info 
            table.append(format_line(line))

    #write file to csv
    create_csv(filename, table)
    




def main(argv):
    #ensure the file name is passed as an argument
    assert argv[1] != "", f"A file name should be given as an argument"
    print(argv[1])
    build_csv_file(argv[1])
    

if __name__ == '__main__':
    main(argv)
