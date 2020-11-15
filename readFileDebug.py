with open('token.txt', 'r') as file:
    data = file.read()

print("data=[%s], length=%d"%(data, len(data)))