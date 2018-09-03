"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "qld": "Queensland", "NSW": "New South Wales", "nsw": "New South Wales",
               "NT": "Northern Territory", "nt": "Northern Territory",
               "WA": "Western Australia", "wa": "Western Australia", "ACT": "Australian Capital Territory",
               "act": "Australian Capital Territory",
               "VIC": "Victoria", "vic": "Victoria", "TAS": "Tasmania", "tas": "Tasmania"}
print(STATE_NAMES)


state = input("Enter short state: ")
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ")

for key, value in STATE_NAMES.items():
    print(key, 'is', value)