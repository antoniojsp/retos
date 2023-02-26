# https://www.hackerrank.com/challenges/three-month-preparation-kit-simple-text-editor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine

# Enter your code here. Read input from STDIN. Print output to STDOUT
class Operations:
    def __init__(self):
        self.current = ""
        self.state = []

    def append(self, val):
        self.current += val
        self.state.append(self.current)

    def delete(self, number):
        end = len(self.current) - number
        new_string = ""
        for i in range(0, end):
            new_string += self.current[i]
        self.current = new_string
        self.state.append(self.current)

    def print_class(self, k):
        print(self.current[k - 1])

    def undo(self):
        if self.state:
            self.state.pop()

        if self.state:
            self.current = self.state[-1]
        else:
            self.current = ""


number = int(input())
op = Operations()

for i in range(number):
    task = input().split(" ")
    if task[0] == "1":
        op.append(task[1])
    elif task[0] == "2":
        op.delete(int(task[1]))
    elif task[0] == "3":
        number = int(task[1])
        op.print_class(number)
    else:
        op.undo()

