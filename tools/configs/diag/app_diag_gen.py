import json
import sys
from diag_job import diag_job, diag_job_global
jobs = {}
global_def = {}
provide = {}

def parse_global_diag_job(obj):
    for key,value in obj["global"].items():
        global_def[key] = diag_job_global(value["service_id"],value["sub_service_max_size"],value["sub_service_min_size"])

def parse_jobs(obj):
    for key,value in obj["job"].items():
        jobs[key] = diag_job(global_def[value["type"]].service_id,value["sub_service_id"])

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
        with open(sys.argv[2], "r") as src_a:
            obj = json.loads(src_a.read())

            if "app" not in obj:
                raise Exception("Main config is not app")
            
            if "include" in obj:
                for item in obj["include"]:
                    include(item)

            obj = obj["app"]
            if "diag" not in obj:
                out_obj["provide"] = {}
                out_obj["require"] = {}
                out.write(json.dumps(out_obj, indent=2))
                return
            name = obj["name"]
            app_id = obj["app_id"]
            out_obj["provide"] = {}
            if "provide" in obj["diag"]:
                for job in obj["diag"]["provide"]:
                    if " as " in job:
                        a = job.split(" as ")
                        out_obj["provide"][name+"/"+a[1]] = {}
                        out_obj["provide"][name+"/"+a[1]]["id"] = str(((int(jobs[a[0]].s_id_list)<<16)+jobs[a[0]].sub_id))
                    else:
                        out_obj["provide"][name+"/"+job] = {}
                        out_obj["provide"][name+"/"+job]["id"] = str(((int(jobs[job].s_id_list)<<16)+jobs[job].sub_id))
            out_obj["require"] = {}
            if "require" in obj["diag"]:
                for job in obj["diag"]["require"]:
                    if " as " in job:
                        a = job.split(" as ")
                        out_obj["require"][name+"/"+a[1]] = {}
                        out_obj["require"][name+"/"+a[1]]["id"] = str(((int(jobs[a[0]].s_id_list)<<16)+jobs[a[0]].sub_id))
                    else:
                        out_obj["require"][name+"/"+job] = {}
                        out_obj["require"][name+"/"+job]["id"] = str(((int(jobs[job].s_id_list)<<16)+jobs[job].sub_id))
        out.write(json.dumps(out_obj, indent=2))


if __name__ == "__main__":
    main()
