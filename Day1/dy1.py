D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new': 3}

D_UNION = {**D2, **D1}

D_INTERSECTION = {k: D1[k] for k in D1 if k in D2}

D_DIFF = {k: D1[k] for k in D1 if k not in D2}

D_MERGE = {}
for k in D1.keys() | D2.keys():
    D_MERGE[k] = D1.get(k,0) + D2.get(k,0)
    
    print("D_UNION =",D_UNION)
    print("D_INTERSECTION =",D_INTERSECTION)
    print("D1-D2 =",D_DIFF)
    print("D_MERGE =",D_MERGE)
