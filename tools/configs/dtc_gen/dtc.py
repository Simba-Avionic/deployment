class DTC:
    def __init__(self,id,desc = "") -> None:
        self.id = id
        self.snapshot_list = []
        self.desc = desc
    def SetDesc(self,desc)-> None:
        self.desc = desc