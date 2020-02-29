# Author: Jordan Torres
# Date: 2/28/20

# input will be a list of all members names, section, and height
masterSingers = [
    ["Alex M", "t1", (6, 0)], 
    ["Lina", "s1", (5, 9)],
    ["Aiden", "b1", (5, 11)],
    ["Katie", "a2", (6, 1)],
    ["Asher", "b2", (6, 7)],
    ["jordan", "t2", (5, 10)],
    ["Alex S", "t2", (5, 9)],
    ["Kendal", "s1", (5, 4)],
    ["Rondea", "b1", (5, 10)],
    ["Ethan", "t1", (5, 8)],
    ["Sophie", "s1", (5, 6)],
    ["Emma", "a2", (5, 6)],
    ["Zoe", "s2", (5, 6)],
    ["Sawyer", "s2", (5, 5)],
    ["Neziah", "a2", (5, 7)],
    ["Breyon", "a1", (5, 5)],
    ["James", "a1", (5, 8)],
    ["Celia", "a1", (5, 6)],
    ["Tyren", "b2", (5, 5)],
    ["J'Viohn", "b2", (5, 10)]
    ]

def separateSections(choir):
    sections = []
    splitSections = []
    for person in choir:
        try:
            section = sections.index(person[1]) # Checks if a persons section exists already
            sectionExists = True
        except ValueError:
            sectionExists = False
            sections.append(person[1])
        
        if sectionExists:
            splitSections[section].append(person) # If this person belongs to a section append them to that section
        else:
            splitSections.append([person])

    return splitSections

def organizeByHeight(splitChoir):
    for section in splitChoir:
        section.sort(key = lambda x: x[2])

    return splitChoir

splitChoir = separateSections(masterSingers)

for section in splitChoir:
    print(section)
print("------------------------------------------------------")

splitChoir = organizeByHeight(splitChoir)

for section in splitChoir:
    print(section)
