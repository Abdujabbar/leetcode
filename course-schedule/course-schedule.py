
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, pre_course in prerequisites:
            graph[course].append(pre_course)

        course_states = [0] * numCourses

        def found_deadlock(node):
            if course_states[node] == 1:
                return True

            if course_states[node] == 2:
                return False

            course_states[node] = 1

            for pre_course in graph[node]:
                if found_deadlock(pre_course):
                    return True

            course_states[node] = 2

            return False

        for i in range(numCourses):
            if found_deadlock(i):
                return False

        return True