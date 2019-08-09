from pymongo import MongoClient
import re

client = MongoClient('120.79.98.187', 27017)
db = client.forex_database
collection = db.forex_all

total = collection.find({'text':{'$regex':"GBP",'$options':"$i"}}).limit(100)

totals = list(total)

def process_url(text):
    if re.search('https://.*', text):
        url = re.findall(' ?https://\S* ?', text)
    else:
        url = None
    text = re.sub(' ?https://\S* ?', 'URLs', text)
    return text, url

i = 1
td = {}

while i < 101:
    for total in totals:
        text = total['text']
        time = total['created_at']
        name = total['user']['name']
        id = total['user']['id']
        text, url = process_url(text)
        if re.match('RT',text):
            text = total['retweeted_status']['text']
            time = total['retweeted_status']['created_at']
            text, url = process_url(text)
        if re.search('#', text):
            text = re.sub('#\S*', re.search('#\S*',text).group()[1:], text)
        if re.search('\$', text):
            text = re.sub('\$\S*', re.search('\$\S*', text).group()[1:], text)
        if re.search('@\s', text):
            text = re.sub('@\S*', 'at', text)
        if re.search('@', text):
            text = re.sub('@\S*', re.search('@\S*', text).group()[1:], text)
        if re.search('\\n', text):
            text = re.sub('\\n\S*', re.search('\\n\S*', text).group()[1:], text)
        if re.search('&amp', text):
            text = re.sub('&amp', 'and', text)
        td[i] = {'time':time,
                 # 'name':name,
                 'id':id,
                 'text':text,
                 'url':url}
        i += 1

for k,v in zip(td.keys(),td.values()):
    print(k,v)

print("......")