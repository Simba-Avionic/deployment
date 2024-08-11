from __future__ import annotations


class data_type:
    def __init__(self,name:str,type_str:str,extra_cpp_lib:list[str] = [],is_struc = False) -> None:
        self.name:str = name
        self.typ_str:str = type_str
        self.extra_cpp_lib:list[str] = extra_cpp_lib
    def DefineVariable(self) -> str:
        return self.typ_str+" "+self.name+";"
    def DeclareVariable(self) -> str:
        return ""
    def GetAsParm(self) -> str:
        return self.typ_str+" "+self.name
    def GetInclude(self) -> list[str]:
        res:list[str] = []
        for include in self.extra_cpp_lib:
            res.append("#include " + include)
        return res
    def GetTypeOnly(self) -> str:
        return self.typ_str
    
class Int8(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"std::int8_t",["<cstdint>"])
        
class Int16(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"std::int16_t",["<cstdint>"])
        
class Int32(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"std::int32_t",["<cstdint>"])
        
class Int64(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"std::int64_t",["<cstdint>"])
        
class Uint8(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"std::uint8_t",["<cstdint>"])
        
class Uint16(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"std::uint16_t",["<cstdint>"])
        
class Uint32(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"std::uint32_t",["<cstdint>"])
        
class Uint64(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"std::uint64_t",["<cstdint>"])
        
class Float32(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"float",)      
 
class Float64(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"double",)

class Bool(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"bool",)         
class String(data_type):
    def __init__(self,name:str) -> None:
        super().__init__(name,"std::string", ["<string>"])           
class Structure(data_type):
    def __init__(self, name: str) -> None:
        path = name.replace(".","/")
        super().__init__(name, "struct",[])
        self.variable_list: dict[str,data_type] = {}
    def AddVariable(self, name:str,variable:data_type):
        if name not in self.variable_list:
            self.variable_list[name] = variable
        else:
            assert False