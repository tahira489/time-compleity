def myfunction(n):
    for i in range(0, n+1):
        print("First Loop")
    print("Time Complexity of 1st is O(n)")

    j = 1
    while(j <= n+1):
        print("Second Loop", j)
        j = j * 2
    print("Time Complexity of 2nd is O(log n)")

    for i in range(0, 100):
        print("Third loop")
    print("Time Complexity of 3rd is O(1)")

def totaltimecomplexity():
    print("First Loop:O(n)")
    print("Second Loop:O(log n)")
    print("Third Loop:O(1)")
    print("Total Time Complexity:O(n)")

# Run the function and analyze its complexity
myfunction(2)
totaltimecomplexity()