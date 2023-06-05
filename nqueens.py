def count_attacking_pairs(state):
    """
    Given a state of the N-Queens problem as a list of tuples (row, column),
    returns the number of pairs of queens that attack each other.
    """
    n = len(state)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i][0] == state[j][0] or \
               state[i][1] == state[j][1] or \
               abs(state[i][0] - state[j][0]) == abs(state[i][1] - state[j][1]):
                # Two queens attack each other if they are in the same row, column, or diagonal
                count += 1
    return count

# just run with below input
N = 8
state = [(1,2), (2,1), (3,3), (4,7), (5,6), (6,8), (7,4), (8,5)]
# copy paste output below, comment above input and run again.
# repeat till answer.
# state = [(1, 4), (2, 1), (3, 3), (4, 7), (5, 6), (6, 8), (7, 2), (8, 5)]
# state = [(1, 4), (2, 1), (3, 7), (4, 3), (5, 6), (6, 8), (7, 2), (8, 5)]
# state = [(1, 4), (2, 2), (3, 7), (4, 3), (5, 6), (6, 8), (7, 1), (8, 5)]

print(count_attacking_pairs(state))

count=0
min_err = count_attacking_pairs(state)
print("current state: {0}".format(state))
print("current error: {0}".format(min_err))
best_state = []
for i in range(N):
    for j in range(i+1, N):
        new_state = [s for s in state]
        new_state[i] = (state[i][0], state[j][1])
        new_state[j] = (state[j][0], state[i][1])
        att = count_attacking_pairs(new_state)
        print("swap {0} with {1} - Error = {2}".format(state[i], state[j], att))
        if att < min_err:
            min_err = att
            best_state = [s for s in new_state]

print("min_err: {0}\nbest state: {1}".format(min_err, best_state))



