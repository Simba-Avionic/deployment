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
            if "diag_address" in obj:
                out_obj["diag_id"] = obj["diag_address"]
            
            out_obj["startup_prio"] = obj["bootMode"]
            if "parms" in obj:
                out_obj["parms"] = obj["parms"]
            else:
                out_obj["parms"] = ""
            out_obj["startup_after_delay"] = 0
            out_obj["bin_path"] = sys.argv[3]
        out.write(json.dumps(out_obj,indent=2))
if __name__ == "__main__":
    main()