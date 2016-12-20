yearcalendar = []
for i in range(1900, 2100):
    yearcalendar.append(i)
monthlist = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# splitstring = ["birthday", "to", "January", "31st", "2017", "6", "a.m.",]
dastring = "birthday to January 31st 2017 6 a.m."
splitstring = dastring.split(' ')
# print(splitstring)

# for count, data in enumerate(splitstring):
#         if data in monthlist:
#             month = data
# splitstring.remove(month)
# print(splitstring)

# for count, data in enumerate(splitstring):
#     if data== "a.m.":
#         try:
#             if int(splitstring[count-2]) not in yearcalendar:
#                 hours = splitstring[count-2]
#                 minutes = splitstring[count-1]
#                 seconds = "00"
#                 # print(hours)
#                 # print("\n")
#                 # print(minutes)
#                 # print("\n")
#                 # print(seconds)
#                 # print("\n")
#             elif int(splitstring[count-1]) not in yearcalendar:
#                 hours = splitstring[count-1]
#                 minutes = "00"
#                 seconds = "00"
#         except:
#             hours = splitstring[count-1]
#             minutes = "00"
#             seconds = "00"
#             # print(hours)
#             # print("\n")
#             # print(minutes)
#             # print("\n")
#             # print(seconds)
#             # print("\n")

for count, data in enumerate(splitstring):
    try:
        if data[-2:] == "st" or data[-2:] == "nd" or data[-2:] == "rd" or data[-2:] == "th":
            print("YOLO")
            print(data[:-2])
            int(data[:-2])
            day = data[:-2]
    except:
        continue

# print(day)

# for count, data in enumerate(splitstring):
#     if data[-2:] == "st" or data[-2:] == "nd" or data[-2:] == "rd" or data[-2:] == "th":
#         print(data[:-2])
    # except:
    #     continue

print(day)