import json

book = {}

book['Megha'] = {'name': 'megha',
                "phone_number":'678989',
                'address':'#143 ,chitrpur'}
book['Vandana'] = {'name': 'Vandana',
                "phone_number":'678989',
                'address':'#143 ,CK'}

print(book)

json_obj = json.dumps(book)
print(json_obj)

with open("C:\\temp\\test.json", 'w') as f:
    f.write(json_obj)

with open("C:\\temp\\test.json", 'r') as f:
    s = f.read()
    book = json.loads(s)
    print(book)
