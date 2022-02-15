import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 2
print("Classes per week:", classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week/classes_per_week)
print("Cost per class:", cost_per_class, type(cost_per_class))
#Part B
variable_list = [2,4,6,8,10]
variable_number = random.choice(variable_list)
print(variable_number)