import Sorting


def main():
    with open("data.txt", 'r') as f:
        data = [int(i) for i in f.read().split()]
        Sorting.heap_sort(data)
        with open("result.txt", 'w') as res:
            for i in data:
                res.write(str(i)+" ")


if __name__ == '__main__':
    main()
