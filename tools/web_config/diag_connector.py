import json
import sys
from deployment.tools.configs.diag.diag_job import diag_job, diag_job_global
from deployment.tools.configs.dtc_gen.dtc import DTC

job_global = {}
dtc_list = {}
jobs = {}
provide_jobs = []
def addDtc(json_object):
    for key,value in json_object.items():
        id = 0
        desc = ""
        if "id" in value:
            id = value["id"]
        elif "id_hex" in value:
            id = int(value["id_hex"],16)
        if "desc" in value:
            desc = value["desc"]
        res = DTC(id,desc)
        for did in value["snapshot_list"]:
            res.snapshot_list.append(jobs[did])
        dtc_list[key] = res

def addJob(json_object):
    name = list(json_object.keys())[0]
    if name in job_global:
        return
    json_object = json_object[name]
    if "desc" in json_object:
        temp = diag_job(json_object["type"],json_object["sub_service_id"],json_object["desc"])
        jobs[name] = temp
    else:
        temp = diag_job(json_object["type"],json_object["sub_service_id"])
        jobs[name] = temp

def addProvide(json_object):
    for value in json_object:
        if value not in provide_jobs:
            provide_jobs.append(value)

def addGlobalJob(json_object):
    name = list(json_object.keys())[0]
    if name in job_global:
        return
    json_object = json_object[name]
    temp = diag_job_global(json_object["service_id"],json_object["sub_service_max_size"],json_object["sub_service_min_size"])
    job_global[name] = temp

with open(sys.argv[1], "w+",encoding="utf-8") as out:
    out_obj = {}
    out_obj["jobs"] = []
    out_obj["dtc"] = []
    for i in range(2,len(sys.argv)):
        with open(sys.argv[i],"r",encoding="utf-8") as src_a:
            obj = json.loads(src_a.read())
            if "app" in obj:
                obj=obj["app"]
            if "diag" in obj:
                obj = obj["diag"]
            if "global" in obj:
                addGlobalJob(obj["global"])
            if "job" in obj:
                addJob(obj["job"])
            if "dtc" in obj:
                addDtc(obj["dtc"])
            if 'provide' in obj:
                addProvide(obj["provide"])
    for key, value in dtc_list.items():
        temp = {}
        temp["name"] = key
        temp["id"] = value.id
        temp["desc"] = value.desc
        temp["snapshot"] = value.snapshot_list
        out_obj["dtc"].append(temp)
    for key, value in jobs.items():
        temp = {}
        temp["name"] = key
        temp["s_id"] = job_global[value.s_id_list].service_id
        temp["sub_id"] = value.sub_id
        temp["desc"] = value.desc
        out_obj["jobs"].append(temp)
    out.write(json.dumps(out_obj, indent=2))