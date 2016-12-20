from datetime import datetime

monthlist = ["january", "jan",
"february", "feb",
"march", "mar",
"april", "apr",
"may",
"june", "jun",
"july", "jul",
"august", "aug",
"september", "sep",
"october", "oct",
"november", "nov",
"december", "dec",
]
if "april" in monthlist:
    print("Its in the list!!!")

datring = "june 1 2005 1:33AM"
datetime_object = datetime.strptime(datring, '%B %d %Y %I:%M%p')
print(type(datetime_object))

splitstring = datring.split(' ')
# print(splitstring)
# for count, data in enumerate(splitstring):
#     if data[:4] == "2005":
#         # splitstring.remove(data)
#         print(data)

# # print(splitstring)