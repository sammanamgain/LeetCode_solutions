class Solution:
    def simplifyPath(self, path: str) -> str:
        dircollection = []
        path = path + '/'
        l = 0
        r = l + 1
        
        while r < len(path):
            if path[r] == '/':
                if path[l + 1:r] == '..':
                    if dircollection:
                        dircollection.pop()
                elif path[l + 1:r] != '.' and path[l + 1:r] != '':
                    dircollection.append(path[l + 1:r])
                l = r
            r += 1
        
        if not dircollection:
            return '/'
        
        result = ''
        for i in dircollection:
            result += '/' + i
        
        return result