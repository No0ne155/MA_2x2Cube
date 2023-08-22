import numpy as np
# Open the file in append mode ('a')
file_path = 'cubedata.txt'
count = 12861872368
ts = 9988
data_to_append = (count, ts)
with open(file_path, 'a') as file:
    file.write(f'{ts} sec, {count} turns'+'\n')  # Write the data to the file and add a newline character
