from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        seen = [False] * N
        
        q = deque([0])
        seen[0] = True
        
        while q:
            room = q.popleft()
            for next_room in rooms[room]:
                if not seen[next_room]:
                    q.append(next_room)
                    seen[next_room] = True
        
        return all(seen)
            