class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        ans = []
        folders.sort()
        ans.append(folders[0])
        
        for folder in folders:
            if (folder + "/").startswith(ans[-1] + "/"):
                continue
            ans.append(folder)
        return ans