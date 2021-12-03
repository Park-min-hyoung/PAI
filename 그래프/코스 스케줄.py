#207
from collections import defaultdict

def dfs(course, discovered, check):

    if course not in discovered:
        discovered.append(course)

    cnt = 0
    for next_c in course_dic[course]:
        if next_c in discovered:
            check.append(False)
            return
        else:
            if cnt == 1:
                check.append(False)
                return
            discovered.append(next_c)
            dfs(next_c, discovered, check)
            cnt += 1

    if check:
        return False
    else:

        return True


numCourses = 3
prerequisites = [[1,0],[0,2]]
course_dic = defaultdict(list)
check = []

for x in prerequisites:
    course_dic[x[0]].append(x[1])

result = dfs(prerequisites[0][0],[],check)
print(result)

# 틀렸음
