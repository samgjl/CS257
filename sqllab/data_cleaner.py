def main():
    print("opening...")
    with open("lab-files/earthquakeData.csv", "r") as f:
        lines = f.readlines()
        print(lines)
    print("writing...")
    with open("lab-files/earthquakeData.csv", "w") as f:
        for line in lines:
            if ",," not in line:
                f.write(line)
                
if __name__ == "__main__":
    main()