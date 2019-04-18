import json

from cmdb.types import BaseType,get_instance

jsonstr='''{
    "types":"cmdb.types.Int",
    "value":1000,
    "options":{
        "max":100000,
        "min":0
    }
}
'''
ipjsonstr='''{
    "types":"cmdb.types.IP",
    "value":"192.168.1.1",
    "options":{
        "prefix":"192.1"
    }
}
'''
obj=json.loads(jsonstr)
print(obj)#返回字典
type=obj["types"]
value=obj["value"]
options=obj["options"]
int=get_instance(type,**options)#解构  max:10000 min:0
print(int.stringfiy(value))

ipobj=json.loads(ipjsonstr)
type=ipobj["types"]
value=ipobj["value"]
options=ipobj["options"]
print("-------------",options)
ip=get_instance(type,**options)
print(ip.stringfiy(value))

