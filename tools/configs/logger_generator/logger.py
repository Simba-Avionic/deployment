import json 
import sys

def check_logger_config(obj):
    if "app_id" not in obj:
        raise Exception("Logger don't have: app_id")
    if "app_des" not in obj:
        raise Exception("Logger don't have: app_des")
    if "log_level" not in obj:
        raise Exception("Logger don't have: log_level")
    if "log_mode" not in obj:
        raise Exception("Logger don't have: log_mode")
    
    

def main():
    with open(sys.argv[1],"w+") as out:
        with open(sys.argv[2],"r") as src_a:
            obj = json.loads(src_a.read())
            if "app" not in obj:
                raise Exception("This is not config for app's")
            obj = obj["app"]
            if "logger" not in obj:
                raise Exception("Logger config not exist in json file")
            check_logger_config(obj["logger"])
            out.write(json.dumps(obj["logger"],indent=2))
            out.close()
    
        
        
if __name__ == "__main__":
    main()