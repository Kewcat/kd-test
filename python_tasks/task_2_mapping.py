# Task: Dictionary Frequency Mapping
# Instructions: Return a dictionary where keys are categories 
# and values are the count of occurrences.

def count_categories(categories):
    # TODO: Write your logic here
    d={}
    for i in categories:
        if i not in d:
            d[i]= 1
        elif i in d:
             d[i]= d[i]+1

    print(d)
    return(d)

# Test Case
data = ['Brakes', 'Engine', 'Brakes', 'Tools', 'Engine', 'Brakes']
# Expected: {'Brakes': 3, 'Engine': 2, 'Tools': 1}
print(count_categories(data))