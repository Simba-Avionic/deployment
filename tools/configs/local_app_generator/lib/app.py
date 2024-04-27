
class App_someip:
    def __init__(self,name, id,port,mode, platform, methods, events,req_methods,req_events) -> None:
        self.id = id
        self.name = name
        self.port = port
        self.mode = mode.split("|")
        self.platform = platform
        self.methods  = {}
        for item in methods:
            self.methods[item["name"]] = {}
            self.methods[item["name"]]["id"] = item["id"]
            if "access_list" in item:
                self.methods[item["name"]]["access_list"] = item["access_list"]
            else:
                self.methods[item["name"]]["access_list"] = []
        self.events  = {}
        for item in events:
            self.events[item["name"]] = {}
            self.events[item["name"]]["id"] = item["id"]
        self.req_methods = req_methods
        self.req_events = req_events