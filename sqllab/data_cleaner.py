def rm_missing_cols(path):
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    
    with open(path, "w") as f:
        for line in lines:
            if ",," not in line:
                f.write(line)
    print("rm_missing_cols complete.")
                
if __name__ == "__main__":
    path = "lab-files/earthquakeData.csv"
    rm_missing_cols(path)