import pygal
from Die import Die

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2,max_result+1):
    frequencie = results.count(value)
    frequencies.append(frequencie)

print(frequencies)

hist = pygal.Bar()
hist.title = 'Results of rolling a D6 and a D10 50000 times.'

hist.x_labels = []
for value in range(2,max_result+1):
    hist.x_labels.append(str(value))


hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6+D10',frequencies)
hist.render_to_file('die_visual.svg')
