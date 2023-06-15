#Assignment-1
import json
class Employee:
  def __init__(self, name, dob, height, city, state):
    self.name = name
    self.dob = dob
    self.height = height
    self.city = city
    self.state = state

  def __str__(self):
    return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"

# Read the JSON file and parse it into a list of dictionaries
with open("hot.json") as f:
  data = json.load(f)
# Create a list of Employee objects from the data
employees = []
for item in data:
  emp = Employee(item["Name"], item["DOB"], item["Height"], item["City"], item["State"])
  employees.append(emp)

# Print the list of Employee objects
for emp in employees:
  print(emp)