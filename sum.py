def sum(a,b):
    
    if b==0:
        return a
    return sum(a+1,b-1)

# testing
if __name__ == "__main__":
    print(sum(2,3))