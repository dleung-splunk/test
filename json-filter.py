import json

if __name__ == "__main__":

    det_str = "detections"
    cnt_str = "count"

    sse_dict ={det_str: [], cnt_str: 0}
    others_dict = {det_str: [], cnt_str: 0}

    sse_prod_list = ['Splunk Enterprise', 'Splunk Enterprise Security', 'Splunk Cloud']
    sse_prod_set = set(sse_prod_list)


    d_file = open('detections.json')
    d_dict = json.load(d_file)
    d_list = d_dict[det_str]
    d_count = d_dict[cnt_str]


    for d in d_list:
        prod_set = set(d['tags']['product'])
        if sse_prod_set & prod_set:
            sse_dict[det_str].append(d)
            sse_dict[cnt_str] += 1
        else:
            others_dict[det_str].append(d)
            others_dict[cnt_str] += 1
    
    with open('sse_out.json', 'w') as sse_file:
        json.dump(sse_dict, sse_file)
    
    with open('others_out.json', 'w') as others_file:
        json.dump(others_dict, others_file)

    print("Total Count: " + str(d_count))
    print("SSE Count: " + str(sse_dict[cnt_str]))
    print("Others Count: " + str(others_dict[cnt_str]))
        
