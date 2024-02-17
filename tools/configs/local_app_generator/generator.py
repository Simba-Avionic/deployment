import json 
from lib.app import App_someip
from lib.platform import Platform
import sys

this_app = App_someip("","",0,"","",[],[],[],[])
apps = {}
platforms = {}
db = {}
def createApp(obj):
    obj_t = obj["app"]
    if "someip" not in obj_t:
        raise Exception("No someip app")
    obj_t = obj_t["someip"]
    req_method = []
    if "req_methods" in obj_t:
        req_method = obj_t["req_methods"]
    req_event = []
    if "req_events" in obj_t:
        req_event = obj_t["req_events"]
    return App_someip(obj["app"]["name"],obj_t["service_id"], obj_t["port"], obj_t["mode"],obj_t["platform"],obj_t["methods"],obj_t["events"],req_method,req_event)
def createPlatform(obj):
    return Platform(obj["platform"]["ip"])

def AddToDB(app,this_app):
    if str(app.id) not in db:
        if app.platform == this_app.platform:
            if "kIPC" in app.mode:
                db[str(app.id)] = {}
                db[str(app.id)]["ip"] = "SIMBA.SOMEIP."+str(app.id)
                db[str(app.id)]["port"] = 0
            else:
                db[str(app.id)] = {}
                db[str(app.id)]["ip"] = platforms[app.platform].ip
                db[str(app.id)]["port"] = app.port
        else:
            if "kUDP" not in app.mode:
                raise Exception("Platform No trace for service: "+str(app.id))
            db[str(app.id)] = {}
            db[str(app.id)]["ip"] = platforms[app.platform].ip
            db[str(app.id)]["port"] = app.port

def FindService(name,this_app):
    service_name = name.split("/")[0]
    method_name = name.split("/")[1]
    app = apps[service_name]
    method_id = app.methods[method_name]
    AddToDB(app,this_app)
    return [app.id,method_id]



def FindSub(name,this_app):
    id_list = []
    for a in apps:
        if name in apps[a].req_events:
            id_list.append(apps[a].id)
            AddToDB(apps[a],this_app)
    return id_list

def FindServiceEvent(name,this_app):
    service_name = name.split("/")[0]
    method_name = name.split("/")[1]
    app = apps[service_name]
    method_id = app.events[method_name]
    AddToDB(app,this_app)
    return [app.id,method_id]


def genConfig(app):
    obj = {}
    obj["service_id"] = app.id
    obj["interface"] = []
    if "kIPC" in app.mode:
        t_obj = {}
        t_obj["ip"] = "SIMBA.SOMEIP."+str(app.id)
        t_obj["port"] = 0
        obj["interface"].append(t_obj)
    if "kUDP" in app.mode:
        t_obj = {}
        if app.platform in platforms:
            t_obj["ip"] = platforms[app.platform].ip
            t_obj["port"] = app.port
            obj["interface"].append(t_obj)
        else:
            raise Exception("Platform not founded")
        
    obj["pub_methods"] = {}
    for key in app.methods.keys():
        obj["pub_methods"][app.name+"/"+key] = {}
        obj["pub_methods"][app.name+"/"+key]["method_id"]= app.methods[key]
    
    obj["pub_event"] = {}
    for key in app.events.keys():
        sub = FindSub(app.name+"/"+key,app)
        obj["pub_event"][app.name+"/"+key] = {} 
        obj["pub_event"][app.name+"/"+key]["event_id"] = app.events[key]
        obj["pub_event"][app.name+"/"+key]["subscribers"] = sub
    obj["req_methods"] = {}
    for m in app.req_methods:
        obj["req_methods"][m] = {}
        [id,method_id] = FindService(m,app)
        obj["req_methods"][m]["service_id"] = id
        obj["req_methods"][m]["method_id"] = method_id
    obj["req_events"] = {}
    for m in app.req_events:
        obj["req_events"][m] = {}
        [id,method_id] = FindServiceEvent(m,app)
        obj["req_events"][m]["service_id"] = id
        obj["req_events"][m]["event_id"] = method_id
        
    obj["db"] = {}
    obj["db"] = db
    return obj

def main():
    
    with open(sys.argv[1],"w+") as out:
        with open(sys.argv[2],"r") as src_a:
            obj = json.loads(src_a.read())
            if "app" not in obj:
                raise Exception("Main config is not app")
            if "someip" not in obj["app"]:
                out.write("{}")
                return
            this_app = createApp(obj)
        for i in range(2,len(sys.argv)):
            with open(sys.argv[i]) as src_b:
                obj = json.loads(src_b.read())
                if "app" in obj:
                    if "someip" in obj["app"]:
                        apps[obj["app"]["name"]] = createApp(obj)
                elif "platform" in obj:
                    platforms[obj["platform"]["name"]] = createPlatform(obj)
                        
                        
        
        print("App "+this_app.name+" loaded")
        print(str(len(apps))+" applications loaded to DB")
        print(str(len(platforms))+" platforms loaded to DB")
        out.write(json.dumps(genConfig(this_app),indent=2))
if __name__ == "__main__":
    main()