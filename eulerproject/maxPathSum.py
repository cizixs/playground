

def maxPathSum(filename):
    prev_max = [0, 0]
    with open(filename, 'r') as f:
        for line in f:
            current_max = [0]
            current_line = [int(num.strip()) for num in line.strip().split()]
            for i in range(len(current_line)):
                current_max.append(max(prev_max[i+1], prev_max[i]) +
                                   current_line[i])
            current_max.append(0)
            prev_max = current_max

    return prev_max

print max(maxPathSum('problem18.txt'))
print max(maxPathSum('p067_triangle.txt'))
