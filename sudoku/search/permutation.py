test = [[1, 2], [3, 4], [5, 6]]
#1 3 4; 1 3 6; 1 4 5; 1 4 6;
#2 3 5; 2 3 6; 2 4 5; 2 4 6;


def permute(list):
    p = []
    for i in range(0, len(list)):
