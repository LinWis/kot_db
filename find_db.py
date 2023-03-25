"""with open("example.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for line in lines:
        for i in range(len(line)):
            if line[i] == "@" and len(line[i:]) > 60:
                info = line[line.find(':', i) + 1:].split(", ")
                if len(info) < 16:
                    print("Bad info")
                else:
                    print("good info")

                for s in info:
                    print(s.strip(), end=" ")

                print("\n")"""

print("123.txt"[:"123.txt".find(".")])
