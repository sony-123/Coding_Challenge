import json
import time
import subprocess


def main():
    m = open('Data.json', 'r')
    jsondata = m.read()

    obj = json.loads(jsondata)
    list = obj['Dependencies']
    d = list[0]
    keys = d.keys()
    lk = []
    lv = []
    values = d.values()
    for i in keys:
        lk.append(i)
    for i in values:
        lv.append(i)

    a='pip install '
    e='=='

    results=[]
    for i in range(len(lk)):
        final = a + lk[i] + e + lv[i]
        results.append(not(subprocess.call(final)))
        time.sleep(10)

    if False in results:
        fail=[]
        for i in range(len(results)):
            if not(results[i]):
                fail.append(lk[i])
        return fail
    return "Success"


if __name__ == '__main__':
    res=main()
    if res!="Success":
        print(*res, sep = "\n")
    else:
        print(res)

