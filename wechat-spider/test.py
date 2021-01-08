di = {"a": 1, "b": {"aa": 2, "bb": 15}}
def strall(data):
    for k,v in data.items():
        if type(v) == dict:
            strall(v)
        else:
            data[k] = str(v)
strall(di)
print(di)

#单引号换双引号
import json
di = json.dumps(di)
print(di)