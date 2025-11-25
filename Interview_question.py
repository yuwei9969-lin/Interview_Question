
#{'hired':{'be':{'to':{'deserve':'I'}}}}
input = input("Please input a dictionary without using reverse: ")
input_value= eval(input)
#print(input_value)

path = []
# using reserve
while isinstance(input_value,dict):
    key = list(input_value.keys())[0]
    path.append(key)
    input_value = input_value[key]

path.append(input_value)

#print(path)

output_value = path[0]
for key in path[1:]:
    output_value = {key: output_value}

print(output_value)
