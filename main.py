from to_ascii import convert_image_to_ascii

txt = convert_image_to_ascii(input('Write image path please\n'), int(input('New width pls\n')))

with open('./' + input('What txt file name do you want ?\n') + '.txt', 'w') as file:
    file.write(txt)

print(txt)
