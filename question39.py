## Bubble Sort: Implement the bubble sort algorithm to sort a list of numbers in ascending order.

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

def main():
    list = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(list))

if __name__ == "__main__":
    main()