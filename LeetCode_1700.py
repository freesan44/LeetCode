class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #暴力法
        while len(sandwiches) != 0 and (sandwiches[0] in students):
            while students[0] != sandwiches[0]:
                students.append(students.pop(0))
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
        return len(students)

if __name__ == '__main__':
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    students = [1, 1, 0, 0]
    sandwiches = [0, 1, 0, 1]
    res = Solution().countStudents(students,sandwiches)
    print(res)