import json
import sys
import random
from deployment.tools.configs.diag.diag_job import diag_job,diag_job_global
from deployment.tools.configs.dtc_gen.dtc import DTC
jobs = {}
global_def = {}
dtc_list = []

def parse_global_diag_job(obj):
    for key,value in obj["global"].items():
        global_def[key] = diag_job_global(value["service_id"],value["sub_service_max_size"],value["sub_service_min_size"])

def parse_jobs(obj):
    for key,value in obj["job"].items():
        jobs[key] = diag_job(global_def[value["type"]].service_id,value["sub_service_id"])

def parse_dtc(obj):
    for key,value in obj["dtc"].items():
        id = 0
        if "id" in value:
            id = value["id"]
        elif "id_hex" in value:
            id = int(value["id_hex"],16)
        res = DTC(id)
        for did in value["snapshot_list"]:
            # res.snapshot_list.append(str(((int(jobs[did].s_id_list)<<16)+jobs[did].sub_id)))
            res.snapshot_list.append(jobs[did])
        dtc_list.append(res)
def include(path):
    with open(path, "r") as file:
        obj = json.loads(file.read())
        if "diag" not in obj:
            return
        if "include" in obj:
            for item in obj["include"]:
                include(item)
        obj = obj["diag"]
        if "global" in obj:
            parse_global_diag_job(obj)
        if "job" in obj:
            parse_jobs(obj)

def main():
    print(sys.argv[1])
    with open(sys.argv[1], "w+") as out:
        out_obj = {}
        out_obj["db"] = []
        for i in range(2,len(sys.argv)):
            with open(sys.argv[i],"r") as in_file:
                obj = json.loads(in_file.read())
                if "diag" not in obj:
                    break
                if "dtc" in obj["diag"]:
                    for path in obj["include"]:
                        include(path)
                    parse_dtc(obj["diag"])
                    
        for dtc in dtc_list:
            item = {}
            temp = hex(dtc.id).upper()
            temp.replace("X","x")
            if(len(temp) < 8):
                temp2 = ""
                for i in range(0,8-len(temp)):
                    temp2+="0"
                temp = "0x"+temp2+temp[2:]
            temp = "0x"+temp[2:]
            item["name"]=temp
            item["id"] = dtc.id
            item["snapshot"] = []
            for did in dtc.snapshot_list:
                item2 = {}
                item2["name"] = did.sub_id
                item2["adress"]=str(((int(did.s_id_list)<<16)+did.sub_id))
                item["snapshot"].append(item2)
            hash = random.getrandbits(128)
            out_obj["hash"] = ("%032x" % hash)
            out_obj["db"].append(item)
        out.write(json.dumps(out_obj, indent=2))


if __name__ == "__main__":
    main()