import csv
import json
import datetime
d = {'name' : 'Foo'}

# Open the CSV
f = open( './datosfic', 'rU' )
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader( f, fieldnames = ( "fieldname0","fieldname1","fieldname2","fieldname3" ))
# Parse the CSV into JSON
#d['date'] = datetime.datetime.now()
#def myconverter(o):
#    if isinstance(o, datetime.datetime):
#        return o.__str__()
#out1=json.dumps(d,default  = myconverter)

out = json.dumps( [ row for row in reader ] )
#out2 =print(out1+out)
print "JSON parsed!"
# Save the JSON
f = open( './parsed.json', 'w')
f.write(out)
print "JSON saved!"
