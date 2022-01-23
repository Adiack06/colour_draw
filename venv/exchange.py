import time
current = 1
end_number = 100
output = ""
outputs =[]
file = open("fizzbuzz.txt", "a")
start = 0
fin = 0
file.truncate(0)
print("what number do you want to go to")
end_number = int(input())
start = time.time()


for i in range(0, end_number):
    output += f"{current}. "
    if current % 3 ==0: output += "fizz"
    if current % 5 ==0: output += "buzz"
    print(output)
    outputs.append(output)
    output = ""
    current += 1

for output in outputs:
    file.write(f"{output}\n")
fin = time.time()
tpf = (fin - start) / (end_number / 1000000)
print(f"{tpf}s per one mega fizz buzz")
print(f"{fin-start}s")