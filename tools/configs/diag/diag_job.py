
class diag_job:
    def __init__(self,s_id_list,sub_id) -> None:
        self.s_id_list = s_id_list
        self.sub_id = sub_id
        pass

class diag_job_global:
    def __init__(self,service_id,max_sub_id,min_sub_id) -> None:
        self.service_id = service_id
        self.max_sub_id = max_sub_id
        self.min_sub_id = min_sub_id