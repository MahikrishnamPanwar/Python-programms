
with open("demo.txt","r") as src:
    with open("dest.txt","w") as dst:
        for line in src:
            dst.write(line)

