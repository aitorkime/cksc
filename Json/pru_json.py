import csv,json

f = open ('datosfic' , 'rU' )
json.dumps(f)
jsonfile = open ('parseado', 'w')

fieldnames = ("t","ws","wg","wd")

reader = csv.DictReader ( f, fieldnames)

for row in reader:
jstr=json.dumps (row, jsonfile)
print (jstr)
#jsonfile.write('\n')
