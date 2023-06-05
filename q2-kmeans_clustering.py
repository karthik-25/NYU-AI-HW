from pprint import pprint
from math import sqrt

def get_lettered_list(l, data_dict):
    c = []
    for pt in l:
        for k, v in data_dict.items():
            if v == pt:
                c.append(k)

    return c

def get_euclid_dist(pt1, pt2):
    return (pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2
    # return sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
    # return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])

# INPUT
# data = [[352,768], [933,1093], [539,192], [293,422], [512,858], [23,444], [4,9], [1077,380], [1033,905], [701,639]]
# data_dict = {"A":[352,768], "B":[933,1093], "C":[539,192], "D":[293,422], "E":[512,858], "F":[23,444], "G":[4,9], "H":[1077,380], "I":[1033,905], "J":[701,639]}
data = [[2959,734], [903,300], [2935,2061], [2118,2313], [1663,984], [789,1370], [61,455], [1341,1480], [2027,1114], [1801,1859], [1480,1252], [1645,1160]]
data_dict = {"A":[2959,734], "B":[903,300], "C":[2935,2061], "D":[2118,2313], "E":[1663,984], 
             "F":[789,1370], "G":[61,455], "H":[1341,1480], "I":[2027,1114], "J":[1801,1859],
             "K":[1480,1252], "L":[1645,1160]}

# centers = [[400,10], [300,700], [800,300]]
# centers = [data_dict["B"], data_dict["D"], data_dict["E"]]
# C1=<750,1500>, C2=<2200,500> C3=<1250,1250>
centers = [[750,1500], [2200,500], [1250,1250]]
num_iterations = 3
# note, no logic to check for convergence, so try different num_iterations to see if it converges
# distance type, uncomment manually above in get_euclid_dist

clusters = {}
print("Initial centers: {0}\n".format(centers))
print("Let 0, 1, 2 be the clusters corresponding to centers above respectively\n")

for i in range(num_iterations):
    print("Iteration {0}".format(i+1))

    for i in range(len(centers)):
        clusters[i] = []

    for pt in data:
        min_dist = float('inf')
        for i in range(len(centers)):
            dist = get_euclid_dist(pt, centers[i])
            # print("distance from {0} to center {1}, {2} = {3}".format(get_lettered_list([pt],data_dict)[0], i, centers[i], dist))
            if dist < min_dist:
                min_dist = dist
                min_c = i

        clusters[min_c].append(pt)
        print("\n{0} belongs to cluster {1}, {2}".format(get_lettered_list([pt],data_dict)[0], min_c, centers[min_c]))
        print("distance: {0}\n".format(min_dist))

    print("Current clusters:")
    for k, v in clusters.items():
        print("cluster {0} at {1} : {2}".format(k, centers[k], get_lettered_list(v, data_dict)))

    print("")

    for c, pts in clusters.items():
        x = 0
        y = 0
        for pt in pts:
            x += pt[0]
            y += pt[1]

        centers[c] = [round(x/len(pts), 2), round(y/len(pts), 2)]

    print("New centers:\n{0}\n".format(centers))

for k, v in clusters.items():
    print("cluster {0} at {1} : {2}".format(k, centers[k], get_lettered_list(v, data_dict)))
