x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"]="Bryant"

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"

# Change the value 20 in z to 30
z[0]["y"]=30


# Iterate Through a List of Dictionaries

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterate_dictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterate_dictionary(students):
    for i in students:
        for key, value in i.items():
            print(key + " - " + value)


#Get Values From a List of Dictionaries


def iterate_dictionary2(first_name,students):
    for i in students:
        print(i["first_name"])

def iterate_dictionary2(last_name,students):
    for i in students:
        print(i["last_name"])


# Create a function print_info(some_dict) that given a dictionary 
# whose values are all lists, prints the name of each key along with
# the size of its list, and then prints the associated values within
# each key's list.

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dojo):
    print(f"{len(dojo['locations'])} LOCATIONS")
    for location in dojo["locations"]:
        print(location)
    print(f"{len(dojo['instructors'])} INSTRUCTORS")
    for instructor in dojo["instructors"]:
        print(instructor)

print_info(dojo)

# print_info(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


