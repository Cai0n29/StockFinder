import requests
import json

line = input('Stock Name: ')
header = {'X-Finnhub-Token': 'ci2sig1r01qmam6busd0ci2sig1r01qmam6busdg'}
r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={line}', headers = header)

rjson = json.loads(r.content)
value = rjson['c']
previous = rjson['pc']
high = rjson['h']
low = rjson['l']

print(line +" "+ 'Current Value: ' + '$' + str(value))
print(line +" "+'Previous Close: ' + '$' + str(previous))
print(line +" "+ 'Highest Price of the Day: ' + '$' + str(high))
print(line +" "+ 'Lowest Price of the Day: ' + '$' + str(low))
