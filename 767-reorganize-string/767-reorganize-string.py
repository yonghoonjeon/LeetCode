class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        # declare list
        res_list = []
        # count character frequencies
        s_dict = Counter(s)
        while s_dict:
            # break rule
            if len(s_dict.keys()) == 1: 
                # len
                if list(s_dict.values())[0] == 1:
                    res_list.append(list(s_dict.keys())[0])
                    res_str = "".join(res_list)
                    return res_str
                elif list(s_dict.values())[0] > 1:
                    return ""
            # top2
            for key, _ in s_dict.most_common(2):
                # put key to the queue
                res_list.append(key)
                # update item
                s_dict[key] -= 1
                # del key if zero values
                if s_dict[key] == 0:
                    del s_dict[key]
        # return
        res_str = "".join(res_list)
        return res_str