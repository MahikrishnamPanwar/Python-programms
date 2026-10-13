
with open("text.txt","r") as f:
    text = f.read()
    print(text)
    words = text.split()
    print(f"Number of words in a file : {len(words)}")

