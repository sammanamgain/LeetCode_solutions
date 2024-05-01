class Solution:
    def simplifyPath(self, path: str) -> str:
        dircollection = []
        path = path + '/'
        l = 0
        r = l + 1
        flag = False

        while r < len(path):
            while path[r] != '/':
                if (path[r] == '.' and path[r + 1] == '.' and path[r + 2] == '.'):
                    r = r + 3
                elif (path[r] == '.' and path[r + 1] == '.' and path[r + 2] == '/' and path[r - 1] == '/'):
                    flag = True
                    r += 1
                    l = r + 2
                    if dircollection:  # Check if the stack is not empty
                        dircollection.pop()
                else:
                    r += 1

            if flag == True:
                flag = False
            else:
                if path[l + 1:r] != '.':
                    dircollection.append(path[l + 1:r])

            if r != len(path) - 1:
                if path[r] == path[r + 1]:
                    r += 1
            l = r
            r += 1

        if not dircollection:
            return '/'

        result = ''
        for i in dircollection:
            if i != '.' and i != '':
                result += ('/' + i)

        if result and result[-1] == '/':
            return result[:-1]
        elif result == "":
            return '/'
        return result