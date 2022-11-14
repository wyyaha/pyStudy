# fr = open("C:/wyy/test.txt", 'r', encoding="UTF-8")
fy = open("C:/wyy/yy.txt", 'w', encoding="UTF-8")

# for line in fr:
#     line1 = line.strip()
#     if line1.split("，")[2] == '语文':
#         continue
#     fw.write(line)
fy.write("1")
# fw.write("\n")
fy = open("C:/wyy/yy.txt", 'w', encoding="UTF-8")
fy.write("2")
# fr.close()
fy.close()
