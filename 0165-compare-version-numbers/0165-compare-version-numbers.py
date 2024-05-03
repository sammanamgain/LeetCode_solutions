class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split('.')
        version2=version2.split('.')

        if len(version1)>len(version2):
            for i in range(len(version1)-len(version2)):
                version2.append(0)
        elif len(version1)<len(version2):
            for i in range(len(version2)-len(version1)):
                version1.append(0)


        for i ,j in zip(version1,version2):
            print(i,j)
            if (int(i)+1)>(int(j)+1):
                return 1
            elif (int(j)+1)>(int(i)+1):
                return -1
            
        return 0

        