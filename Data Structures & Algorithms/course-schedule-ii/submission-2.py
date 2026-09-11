class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        if not numCourses:
            return res
        course_req = {course: [] for course in range(numCourses)}
        for a, b in prerequisites:
            course_req[a].append(b)
        visiting, visited = set(), set()
        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for prereq in course_req[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            
