from __future__ import annotations
import sys
import os
import copy
import json
from deployment.tools.ara.common.common_parser import CommonParser
from deployment.tools.ara.app.adaptive_application_db import AdaptiveApplicationDb
from deployment.tools.ara.app.adaptive_application_extractor import AdaptiveApplicationExtractor
from deployment.tools.ara.common.data_structure import data_type
from deployment.tools.ara.someip.lib.someip_db import *
def LoadJson(path:str):
    CommonParser.LoadJson(path)
def CreateDir(start:str,finish:str):
    for p in finish.split("/"):
            start+="/"+p
            try:
                os.makedirs(start)
            except:
                pass

if __name__ == "__main__":
    out_path = sys.argv[1]
    src_path = ""
    for val in sys.argv:
        if ".json" in val:
            if os.path.isfile(val):
                with open(val,"r") as file:
                    json_obj = json.load(file)
                    if "adaptive_application" in json_obj:
                        if len(src_path) == 0:
                            src_path = val
                        else:
                            raise Exception("Multiple Adaptive App model found!")
    if len(src_path) != 0:                
        LoadJson(src_path)
        app_name = list(AdaptiveApplicationDb().app_list.keys())[0]
        app = AdaptiveApplicationDb().app_list[list(AdaptiveApplicationDb().app_list.keys())[0]]
        # for p in app_name.split("."):
        #     out_path+="/"+p
        #     os.makedirs(out_path)
        service_list: dict[str,Service] = {}
        struct_list: dict[str,data_type] = {}
        for k,s in app.provide_someip.items():
            if s.item.name not in service_list:
                service_list[s.item.name] = s.item
                CreateDir(copy.copy(out_path),s.item.name.replace(".","/"))
                for m in s.item.methods:
                    if m.in_parm.typ_str == "struct":
                        if m.in_parm.name not in struct_list:
                            struct_list[m.in_parm.name] = m.in_parm
                    if m.out_parm.typ_str == "struct":
                        if m.out_parm.name not in struct_list:
                            struct_list[m.out_parm.name] = m.out_parm
                            CreateDir(copy.copy(out_path),m.out_parm.name.replace(".","/"))
                for m in s.item.events:
                    if m.out_parm.typ_str == "struct":
                        if m.out_parm.name not in struct_list:
                            struct_list[m.out_parm.name] = m.out_parm
                            CreateDir(copy.copy(out_path),m.out_parm.name.replace(".","/"))
        
        
    else:
        raise Exception("Adaptive app def not found!")