from collections import deque
class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1

        ds = deque(list(s))

        while ds:
            if len(ds) == 1:
                return 1
            if ds and len(ds) > 1 and ds[-1] != ds[0]:
                return len(ds)

            while len(ds) > 1 and ds[1] == ds[0]:
                ds.popleft()
            else:
                if ds:
                    ds.popleft()

            while len(ds) > 1 and ds[-1] == ds[-2]:
                ds.pop()
            else:
                if ds:
                    ds.pop()

        return len(ds)