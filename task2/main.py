import random

def binary_search(arr, x):
    step = 0
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        step += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
            print(arr[mid])
        elif arr[mid] > x:
            high = mid - 1
            print(arr[mid])
        else:
            print ("Bingo!")
            return (step, arr[mid-1])
    return -1

def main():
    arr = [0.04, 0.53, 0.86, 1.23, 2.98, 3.01, 4.25, 5.31, 9.02, 11.58, 12.72, 12.77, 14.04, 16.64, 18.54, 20.31, 
          22.18, 23.54, 23.54, 24.2, 24.32, 25.28, 25.33, 25.74, 26.01, 26.61, 27.09, 28.12, 28.28, 30.5, 30.54, 31.01, 31.34, 32.52, 34.02,
          34.16, 34.22, 34.23, 37.77, 39.62, 41.04, 41.81, 42.73, 44.58, 45.02, 45.31, 46.8, 47.55, 49.75, 49.83]
    x = 28.12
    result = binary_search(arr, x)
    if result != -1:
        print(f"I made  {result[0]} steps. \nPrevious value: {result[1]}")
    else:
        print("Element is not present in array")


if __name__ == "__main__":
    main()
