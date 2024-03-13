import json 
import sys

def main():
    
    with open(sys.argv[1],"w+") as out:
        out_obj = {}
        with open(sys.argv[2],"r") as src_a:
            obj = json.loads(src_a.read())
            
            if "app" not in obj:
                raise Exception("Main config is not app")
            obj = obj["app"]
            if "diag" in obj:
                if "service_id" in obj["diag"]:
                    out_obj["service_id"] = obj["diag"]["service_id"]
        out.write(json.dumps(out_obj,indent=2))
if __name__ == "__main__":
    main()