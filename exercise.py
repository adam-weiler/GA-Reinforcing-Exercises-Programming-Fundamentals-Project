from project import project

# print(project)  # The entire dictionary
# print(project.keys())  # dict_keys(['committee', 'title', 'due_date', 'id', 'steps'])
# print(project['committee'])  # ['Stella', 'Salma', 'Kai']
# print(project['title'])  # "Very Important Project"
# print(project['due_date'])  # "December 14, 2019"
# print(project['id'])  # 3284
print(f"The original project: {project['steps']}\n")  # A list of 9 steps
# print(len(project['steps']))  # 9

number_of_people = len(project['committee'])  # 3
# number_of_tasks = len(project['steps'])  # 9

for index, step in enumerate(project['steps']):  # For each step in steps.
    # print(value)
    # print(index % 3)
    project['steps'][index]['person'] = project['committee'][index % number_of_people]  # The current project is assigned to one of 3 committee members.

print(f"The new project: {project['steps']}")
