from collections import deque,defaultdict
class Solution(object):
    def findItinerary(self, tickets):

        def build_graph(tickets):
            G = defaultdict(list)
            for S, E in tickets:
                G[S].append(E)
            for A in G:
                G[A].sort(reverse=True)
                G[A] = deque(G[A])
            return G

        def dfs(G, S):
            trip.append(S)
            if len(trip) == length:
                return True
            if S in G:
                queue=G[S]
                for i in xrange(len(queue)):
                    A = queue.pop()
                    if dfs(G, A):
                        return True
                    queue.appendleft(A)
            trip.pop()
            return False


        G = build_graph(tickets)
        trip, length = [], len(tickets) + 1
        dfs(G, "JFK")
        return trip