#Problem - https://leetcode.com/problems/course-schedule/

from collections import defaultdict

class CourseGraph:
    def __init__(self, numCourses) -> None:
        self.numCourses = numCourses
        self.prereqGraph = defaultdict(list)
    def addPrereq(self, crs, prereq):
        self.prereqGraph[crs].append(prereq)
    def isCyclic(self, crs, visited):
        visited[crs] = True
        for prereq in self.prereqGraph[crs]:
            if visited[prereq]:
                return True
            elif self.isCyclic(prereq, visited):
                return True
        visited[crs] = False
        self.prereqGraph[crs] = []
        return False
    def canFinishAllCourses(self):
        visited = [False]*self.numCourses
        for crs in range(self.numCourses):
            if self.isCyclic(crs, visited):
                return False
        return True

if __name__ == "__main__":
    courseGraph = CourseGraph(5)
    prereqMap = [[1,4],[2,4],[3,1],[3,2]]
    for crs, prereq in prereqMap:
        courseGraph.addPrereq(crs, prereq)
    print(courseGraph.canFinishAllCourses())