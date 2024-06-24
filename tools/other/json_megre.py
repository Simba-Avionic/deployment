import json
import sys

with open(sys.argv[1], "w+",encoding="utf-8") as out:
    jobs = []
    dtcs = []
    platform = []
    out_json = {}
    for i in range(2,len(sys.argv)):
        
        with open(sys.argv[i],"r",encoding="utf-8") as src_a:
            obj = json.loads(src_a.read())
            if "platform" in obj:
                platform.append(obj["platform"])
            if "jobs" in obj:
                for item in obj["jobs"]:
                    jobs.append(item)
            if "dtc" in obj:
                for item in obj["dtc"]:
                    dtcs.append(item)
    out_json["platform"] = platform[0]              
    out_json["jobs"] = jobs 
    out_json["dtc"] = dtcs     
    json.dump(out_json, out, indent=4)
 