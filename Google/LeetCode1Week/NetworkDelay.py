class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(n+1)}
        for u,v,w in times:
            graph[u].append((v,w))
        import heapq
        heap = [(0,k)]
        heapq.heapify(heap)
        visit= {}
        while heap:
            time, dest = heapq.heappop(heap)
            if dest in visit:
                continue
            visit[dest] = time
            for nxt_dest,nxt_time in graph[dest]:
                if nxt_dest not in visit:
                    heapq.heappush(heap,(nxt_time+time,nxt_dest))
        print(visit)
        if len(visit) == n:
            return max(visit.values())
        return -1

        