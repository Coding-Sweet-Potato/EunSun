def migratoryBirds(arr):
    # Write your code here
    dict_id ={'1':0, '2':0, '3':0, '4':0, '5':0}
    for x in arr:
       dict_id[str(x)] += 1

    dict_id = sorted(dict_id.items(), key=lambda x: x[1], reverse=True)
    for key, value in dict_id:
        if value >=1:
            return key
