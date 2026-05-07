

def display_main_menu():
    print("Enter some numbers SEPARATED by commas eg(5, 67, 69)")
    
def calc_average(floatnumbers):
    average = sum(floatnumbers)/len(floatnumbers)
    print(average)

def get_user_input():
    numbers=input()
    stringnumbers = numbers.split(", ")
    floatnumbers = []
    for item in stringnumbers:
        floatnumbers.append(float(item))
    return floatnumbers

def find_min_max(floatnumbers):
    print(f"{min(floatnumbers)}")
    print(f"{max(floatnumbers)}")
    return min(floatnumbers), max(floatnumbers)

def sort_temperature(floatnumbers):
    print(sorted(floatnumbers))

def calc_median_temperature(floatnumbers):
    sortnumbers = sorted(floatnumbers)
    middle = len(sortnumbers) // 2
    if len(sortednumbers) % 2 == 0:
        median = (sortnumbers[middle - 1] + sortnumbers[middle]) / 2
    else: median = sortnumbers[middle]
    print(median)