# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    # TODO: Write your logic here safely
    for i,k in data.items():
       for j,l in k.items():
            for o, p in l.items():
                return(p)

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))