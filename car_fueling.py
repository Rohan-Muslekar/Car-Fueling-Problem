#python3
def min_refills(n, a, dist_with_full_tank):
    num_refills = 0
    current_refills = 0
    last_refills = 0
    #print("Stops where you need to get refilling:")
    while current_refills <= (n):
        last_refills = current_refills
        while (current_refills <= n and (a[current_refills + 1] - a[last_refills]) <= dist_with_full_tank):
                current_refills = current_refills + 1

        #print(a[last_refills])
        if current_refills == last_refills:
            # This happens when gas station is far away that even full tank of 
            # fuel could not make up
            return -1
        if current_refills <= n:
            num_refills = num_refills + 1
    return num_refills

def start():
    #print("Give n:")
    B = int(input())
    L = int(input())
    n = int(input())
    #print("Give gas station stops in kms:")
    a = list(map(int, input().split()))
    a.insert(0,0)
    a.append(B)
    n = n
    #print("Number of refilling required:")
    print(min_refills(n, a, L))

if __name__ == "__main__":
    start()
