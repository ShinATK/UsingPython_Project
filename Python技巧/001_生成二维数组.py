
def createArray2D(w, h):
    return [[0] *w for _ in range(h)]

def show(arr):
    for line in arr:
        print(line)
    
def main():
    a1 = createArray2D(5, 5)
    show(a1)

if __name__ == '__main__':
    main()