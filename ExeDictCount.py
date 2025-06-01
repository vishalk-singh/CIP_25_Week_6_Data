"""
File: ExeDictCount.py
Name: Vishal Singh
--------------------------
"""
from datetime import datetime
def main():
    marksheet = [
        {'Name': 'Vishal',
        'Gender': 'Male',
        'DOB': 'May 1984'}, # index 0
        {'Name': 'Ayesha',
         'Gender': 'Female',
         'DOB': 'June 1985'}, # Index 1
        {'Name': 'Ashley',
         'Gender': 'Female',
         'DOB': 'July 1986'},# Index 2
        {'Name': 'Chris',
         'Gender': 'Male',
         'DOB': 'August 1987'},
        {'Name': 'Karel',
         'Gender': 'Male',
         'DOB': 'September 1988'},
        ]
    gender_count(marksheet)
    born_before_june(marksheet)



def gender_count(marksheet):
    female_count = 0
    male_count = 0
    for i in range(len(marksheet)):
        if marksheet[i].get('Gender') == "Female":
            female_count += 1
        elif marksheet[i].get('Gender') == "Male":
            male_count += 1
    print(f'There are {female_count} female students and {male_count} male students in the class.')

def born_before_june(marksheet):
    for student in marksheet:
        dob_str = student['DOB']  # e.g., "May 1984"
        dob_date = datetime.strptime(dob_str, "%B %Y")  # Convert to datetime object

        # Check if month is between January (1) and June (6)
        if 1 <= dob_date.month <= 6:
            print(f"{student['Name']} was born between Jan and June: {dob_str}")
        else:
            print(f"{student['Name']} was NOT born between Jan and June: {dob_str}")
if __name__ == '__main__':
    main()