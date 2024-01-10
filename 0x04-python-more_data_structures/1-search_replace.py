#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def tmp_sr_elm(elm):
        return (elm if elm != search else replace)
    return list(map(tmp_sr_elm, my_list))
