tasks = []
text = input()

while text !='End':
    command = text
    tokens = command.split('-', maxsplit=1)
    priority = int(tokens[0])
    task = tokens[1]
    tasks.append((priority, task))
    text = input()

#task_in_priority = []

#for priority, task in sorted(tasks):
    #task_in_priority.append(task)
#print(task_in_priority)



task_in_priority = [task for priority, task in sorted(tasks)]
print(task_in_priority)