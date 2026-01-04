def betterCounter(FILE_NAME):
    d = {}
    with open(FILE_NAME, "r") as f:
        for word in f.readlines():
            if not d.get(word, None):
                d[word] = 1
                continue

            d[word] += 1
    
    print(d)

def main():
    betterCounter(f"{__file__}")


if __name__ == "__main__":
    main()
