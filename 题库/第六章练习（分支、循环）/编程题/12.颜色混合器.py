primary_color_1 = input()
primary_color_2 = input()

primary_colors = ['red', 'blue', 'yellow']
mix_colors = {
    'bluered': 'purple',
    'redyellow': 'orange',
    'blueyellow': 'green'
}

if primary_color_1 not in primary_colors or primary_color_2 not in primary_colors:
    print('error')
else:
    input_colors = [primary_color_1, primary_color_2]
    input_colors.sort()
    input_colors = ''.join(input_colors)
    print(mix_colors[input_colors])
