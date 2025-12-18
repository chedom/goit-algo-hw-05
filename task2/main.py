from search import binary_search


def main():
    arr = [2.1, 3.5, 4.7, 10.44, 40.89]

    print(f"Element 3.6 search {binary_search(arr, 3.6)}")  # (3, 4.7)
    print(f"Element 51.2 search {binary_search(arr, 51.2)}")  # (3, None)
    print(f"Element 1.12 search {binary_search(arr, 1.12)}")  # (3, 2.1)


if __name__ == '__main__':
    main()
