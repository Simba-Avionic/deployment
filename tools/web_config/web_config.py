import json
import sys

with open(sys.argv[1], "w+",encoding="utf-8") as out:
    json_list = []
    for i in range(2,len(sys.argv)):
        with open(sys.argv[i],"r",encoding="utf-8") as src_a:
            obj = json.loads(src_a.read())
            json_list.append(obj)
    out.write(json.dumps(json_list, indent=2))