from hash_table import HashTable


def main():
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)

    print(H.get("apple"))   # Виведе: 10
    print(H.get("orange"))  # Виведе: 20
    print(H.get("banana"))  # Виведе: 30
    H.delete("banana")
    print(H.get("banana"))  # Виведе: None


if __name__ == '__main__':
    main()
