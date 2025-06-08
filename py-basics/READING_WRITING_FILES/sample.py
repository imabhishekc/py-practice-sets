"""
Writing about Formula 1 using python files operation.
"""

with open('sample.txt', 'w') as file:
    file.write("Formula 1 (F1) racing is the highest class of international single-seater auto racing. \nIt features cutting-edge technology, elite drivers, and races held on tracks across the world. \nEach season, teams compete in Grand Prix events to earn points toward the World Championship. \nSpeed, strategy, and innovation play crucial roles in every race. \nF1 is known for its thrilling overtakes, high-speed corners, and passionate fanbase.")

file.close() # It releases the occupied resources.


"""
Let's read the above created .txt file
"""

with open('sample.txt', 'r') as f:
    print(f.read())

f.close() 