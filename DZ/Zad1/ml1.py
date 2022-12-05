import re
from PIL import Image

with open("encoded_string2.txt", "r") as input_file:
  encoded_string = input_file.read()

decoded_string = ""

# Koristi se regularni izraz za poklapanje grupa brojeva poslije kojih slijedi znak
# Za svako poklapanje, dodaje se znak u dekodirani string onoliko puta koliko se navodi brojevima
for match in re.finditer(r"\d+[A-Z]", encoded_string):
  decoded_string += int(match.group(0)[:-1]) * match.group(0)[-1]

with open("decoded_string.txt", "w") as output_file:
  output_file.write(decoded_string)


value = decoded_string
cmap = {'A': (255,255,255),
        'B': (0,0,0)}
data = [cmap[letter] for letter in value]
img = Image.new('RGB', (100, len(value)//100), "white")
img.putdata(data)
img.save('MarinoLinic.bmp', 'bmp')


compression_ratio = len(decoded_string) / len(encoded_string)

str_compression_ratio = "Omjer kompresije: " + str(compression_ratio)

with open("omjer_kompresije.txt", "w") as output_file:
  output_file.write(str_compression_ratio)