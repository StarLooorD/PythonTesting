import json

with open('json_example.json', 'r') as f:  # opening file
    parsed_json = json.load(f)  # parsing json with "load" method

# Task 1

config_gp_data = {}  # creating empty dictionary (gp - global parameters)

for elem in parsed_json['Configuration']:  # adding each item of the section to our dictionary
    if not isinstance(parsed_json['Configuration'][elem], dict):  # checking if the value is not dictionary
        config_gp_data[elem] = parsed_json['Configuration'][elem]

print("\n")
print("Example storing data:")  # now its data stored as dictionary
print(config_gp_data)

# Task 2

tagger_data = {}  # creating empty dictionary

for elem in parsed_json['Configuration']['Components']['Tagger']:  # adding each item of the section to our dictionary
    tagger_data[elem] = parsed_json['Configuration']['Components']['Tagger'][elem]

print("\n")
print("Example storing data:")  # now its data stored as dictionary
print(tagger_data)


# Task 3

def transformer(line):  # function for replacing GP reference with their data (returns string)
    if type(line) == int:
        return str(line)
    else:
        reference = []
        new_arr = []
        is_global = False

        line_arr = line.split(" ")
        for i in range(len(line_arr)):
            if line_arr[i] == "{{":
                is_global = True
                reference = line_arr[i + 1].split(".")

        if is_global:
            index = 0
            while line_arr[index] != "{{":
                new_arr.append(line_arr[index])
                index += 1

            new_arr.append(parsed_json[str(reference[0])][str(reference[1])])
            return " ".join(new_arr)
        else:
            return line


print("\n")
for key in parsed_json['Flows']:  # for each subsection in Flows section
    for i in range(len(parsed_json['Flows'][key]['actions'])):  # to define power of list in action section
        for key2 in parsed_json['Flows'][key]['actions'][i]:  # for each subsection in actions section
            print(key2 + " - " + transformer(parsed_json['Flows'][key]['actions'][i][key2]))  # printing line separated
        print("\n")
