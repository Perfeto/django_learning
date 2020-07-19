class BuildingStatusItemModel:
    def __init__(
            self,
            id_ob,
            name_obj,
            addr_obj,
            cat_obj,
            count_items_oper_no,
            count_items_oper_breach,
            count_items_oper_accepted,
            groups_arr
    ):
        self.idObj = id_ob
        self.nameObj = name_obj
        self.addrObj = addr_obj
        self.catObj = cat_obj
        self.countItemsOperNo = count_items_oper_no
        self.countItemsOperBreach = count_items_oper_breach
        self.countItemsOperAccepted = count_items_oper_accepted
        self.GroupsArr = groups_arr
