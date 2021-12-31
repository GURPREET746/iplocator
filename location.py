from typing import Collection
import geocoder
import pymongo


def traceLocation(ipaddress):
    
    g = geocoder.ip(str(ipaddress))

    address = g.latlng

    result = {'ip':ipaddress,
              'city': g.city,
              'country': g.country,
              'state': g.state,
              'postal': g.postal,
              'lat': float(address[0]),
              'long': float(address[1])}

    return(result)
# print(traceLocation('103.110.254.20'))

def storeIp(ipadd):
    data = {"ipaddress":ipadd}
    client = pymongo.MongoClient('mongodb+srv://keshav123:keshav123@cluster0.hmqyt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = client['ipdata']
    collection = db['storedata']
    collection.insert_one(data)
    
def getData():
    client = pymongo.MongoClient('mongodb+srv://keshav123:keshav123@cluster0.hmqyt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = client['ipdata']
    collection = db['storedata']
    data = collection.find({},{'ipaddress':1,'_id':0})
    ipData = []
    for i in data:
        ipData.append(i['ipaddress'])
    return ipData

storeIp('103.110.254.20')