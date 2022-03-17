#!/usr/bin/env python3
#Yash Kapoor
#will copy whatever the input file looks like a replace keywords with the corresponnding thing in the .crs files

#import systems commands
import sys
#import operating system commands
import os
#import global commands
import glob
#import research commands
import re

#checks if the correct number of inputs have been entered
if len(sys.argv) != 5:
    print("Usage: " + sys.argv[0] + " <dir> <template> <date> <output_dir>")
    sys.exit(1)

#giving variable names to the sys.argv's for code
input_dir = sys.argv[1]
template_file = sys.argv[2]
date_input = sys.argv[3]
output_dir = sys.argv[4]

#checks to see if input_dir is a directory
if not os.path.isdir(input_dir):
    print("Error: " + input_dir + " is not a directory.")
    sys.exit(1)


#creates an output dir if it's not there
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

#get the .crs files
crs_files = glob.glob(input_dir + "/*.crs")

#accessing the .crs files, assigning them to variables, and then checking if the number of students is more than 30
for crs in crs_files:
    print("filename = %s" % crs)
    try:
        with open(crs, "r") as f:
            # assigns the different info in the .crs files to specific variables
            dept_code,dept_name=f.readline().split(" ",1)
            dept_name = dept_name.strip()
            course_name=f.readline().rstrip()
            course_sched,course_start,course_end=f.readline().split(" ", 2)
            course_end = course_end.strip()
            credit_hours = f.readline().rstrip()
            num_students = f.readline().rstrip()
            if(int(num_students) > 30):
                tf=open(template_file,"r")
                output_file=crs[7:-4]+".warn"
                o_F=open(output_dir+"/"+output_file,"w")
                data=tf.read()
                data=data.replace("[[dept_code]]",dept_code)
                data=data.replace("[[dept_name]]",dept_name)
                data=data.replace("[[course_name]]",course_name)
                data=data.replace("[[course_sched]]",course_sched)
                data=data.replace("[[course_start]]",course_start)
                data=data.replace("[[course_end]]",course_end)
                data=data.replace("[[credit_hours]]",credit_hours)
                data=data.replace("[[num_students]]",num_students)
                data=data.replace("[[date]]",date_input)
                data=data.replace("[[course_num]]",crs[10:-4])

                o_F.write(data)
                o_F.close()
                tf.close()

    except FileNotFoundError:
        print("error")
    except ValueError:
        print("Value error oh no")
