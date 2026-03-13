#1. basic function with return
def celcius_to_fahrenhiet(celcius: float)-> float:
    """convert celcius to fahrenhiet"""
    return (celcius * 9/5) + 32

#2. Defaut parameters
def create_user(name: str, role: str = "viewer", active: bool = True) -> dict:
    """create user profile dictionary"""
    return {
        "name": name,
        "role": role,
        "active": active
    }   

#3. *args - variable positional argument
def total_score(*score : float) -> float:
    """return total of scrores"""
    return sum(score)

#4. **kwargs - variable keyword argument
def display_info(**details) -> None:
    """print all key value pai passed"""
    for key, value in details.items():
        print(f"{key}: {value}")    

#5. Lamba - sort the list based on a field
students = [
    {"name": "sathya", "age": 20},
    {"name": "ram", "age": 22},
    {"name": "joy", "age": 67},
    {"name": "akshay", "age": 34}
]

students.sort(key=lambda student: student["age"])
print(students)

#run it
print(celcius_to_fahrenhiet(37))
print(create_user("sathya"))    
print(total_score(10,20,30,20))
      