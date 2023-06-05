from pprint import pprint
from math import sqrt

def find_cluster_dist_single_linkage(cluster1, cluster2):
    min_dist = 10000000000
    
    for pt1 in cluster1:
        for pt2 in cluster2:
            dist = (pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2
            # dist = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
            # dist = abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])
            if dist < min_dist:
                min_dist = dist

    return min_dist

def find_cluster_dist_complete_linkage(cluster1, cluster2):
    max_dist = -1
    
    for pt1 in cluster1:
        for pt2 in cluster2:
            dist = (pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2
            # dist = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
            # dist = abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])
            if dist > max_dist:
                max_dist = dist

    return max_dist

def get_lettered_cluster(cluster, data_dict):
    c = []
    for pt in cluster:
        for k, v in data_dict.items():
            if v == pt:
                c.append(k)

    return c

# INPUT
# data = [[352,768], [933,1093], [539,192], [293,422], [512,858], [23,444], [4,9], [1077,380], [1033,905], [701,639]]
# data_dict = {"A":[352,768], "B":[933,1093], "C":[539,192], "D":[293,422], "E":[512,858], "F":[23,444], "G":[4,9], "H":[1077,380], "I":[1033,905], "J":[701,639]}
# data = [[2959,734], [903,300], [2935,2061], [2118,2313], [1663,984], 
#         [789,1370], [61,455], [1341,1480], [2027,1114], [1801,1859], 
#         [1480,1252], [1645,1160]]
# data_dict = {"A":[2959,734], "B":[903,300], "C":[2935,2061], "D":[2118,2313], "E":[1663,984], 
#              "F":[789,1370], "G":[61,455], "H":[1341,1480], "I":[2027,1114], "J":[1801,1859],
#              "K":[1480,1252], "L":[1645,1160]}

data = [[1,6], [1002,20], [498,651], [6,10], [510,622], 
        [503,632], [4,9], [1010,25], [1006,30], [502,680]]
data_dict = {"A":[1,6], "B":[1002,20], "C":[498,651], "D":[6,10], "E":[510,622],
             "F":[503,632], "G":[4,9], "H":[1010,25], "I":[1006,30], "J":[502,680]}

num_clusters = 3
linkage = "single" # "single" or "complete"
# for distance type - euclidean distance squared, euclidean distance, manhattan distance
# uncomment manually in both function above

clustered_data = {}
for i in range(len(data)):
    clustered_data[i] = [data[i]]


while(len(clustered_data) > num_clusters):
    min_dist = 10000000000

    for i in clustered_data.keys():
        # Euclidean distance squared for p, q of =(p_x - q_x)^2 + (p_y - q_y)^2
        for j in clustered_data.keys():

            if clustered_data[i] != clustered_data[j]:
                
                # single linkage
                if linkage == "single":
                    dist = find_cluster_dist_single_linkage(clustered_data[i], clustered_data[j])
                
                # complete linkage
                if linkage == "complete":
                    dist = find_cluster_dist_complete_linkage(clustered_data[i], clustered_data[j])

                # print("distance between cluster {0} and cluster {1} = {2}".format(get_lettered_cluster(clustered_data[i], data_dict), get_lettered_cluster(clustered_data[j], data_dict), dist))

                if dist < min_dist:
                    min_dist = dist
                    min_p = i
                    min_q = j

    print("\nclosest two clusters: {0} and {1}".format(get_lettered_cluster(clustered_data[min_p], data_dict), get_lettered_cluster(clustered_data[min_q], data_dict)))
    print("distance between them = {0}".format(min_dist))
    print("merge them into a cluster. Current clusters:\n")

    clustered_data[min_p] = clustered_data[min_p] + clustered_data[min_q]
    del clustered_data[min_q]

    # pprint(clustered_data)

    for k, v in clustered_data.items():
        print(get_lettered_cluster(v, data_dict))

    print('\n')
