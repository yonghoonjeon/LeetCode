class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set([])
        tables = collections.defaultdict(lambda :collections.defaultdict(int))
        
        # for every order
        for order in orders:
            # customer name
            customerName = order[0]
            # table number
            tableNumber = order[1]
            # food item
            foodItem = order[2]
            
            foods.add(foodItem)
            tables[int(tableNumber)][foodItem] += 1    
        tables = sorted(tables.items(), key=lambda x:x[0])
        foods = sorted(list(foods))
        
        ans = [["Table"]]
        ans[0].extend(foods)
        
        for k, v in tables:
            cur_ans = [str(k)]
            for food in foods:
                cur_ans.append(str(v[food]))
            ans.append(cur_ans)
            
        return ans    