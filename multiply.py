def multiply(a,b):
    
    if b==0:
        return 0
    return a + multiply(a,b-1)

# testing
if __name__ == "__main__":
    print(multiply(2,3))