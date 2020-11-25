# essentials libraries
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# khana count of 8 upazillas
khana_count = [
    1315,
    8159,
    3777,
    949,
    182,
    3623,
    599,
    1685
]

# 8 upazillas list
upazillas = (
    'Singair' + "\n" + str(khana_count[0]),
    'Daudkandi' + "\n" + str(khana_count[1]),
    'Sujanagar' + "\n" + str(khana_count[2]),
    'Pirgacha' + "\n" + str(khana_count[3]),
    'Madhabpur' + "\n" + str(khana_count[4]),
    'Dacope' + "\n" + str(khana_count[5]),
    'Nalcity' + "\n" + str(khana_count[6]),
    'Muktagacha' + "\n" + str(khana_count[7])
    )
y_pos = np.arange(len(upazillas))

bar_lists = plt.bar(y_pos, khana_count)

# set individual colors for individual upazillas
# Singair upazilla -> violet
bar_lists[0].set_color('#EE82EE')
# bar_lists[0].label('Zahid')

# Daudkandi upazilla -> Indigo
bar_lists[1].set_color('#4b0082')

# Sujanagar Upazilla -> blue
bar_lists[2].set_color('#0000ff')

# Pirgacha upazilla -> green
bar_lists[3].set_color('#008000')

# Madhabpur upazilla -> yellow
bar_lists[4].set_color('#ffff00')

# Dacope upazilla -> orange
bar_lists[5].set_color('#ffa500')

# Nalcity upazilla -> red
bar_lists[6].set_color('#ff0000')

# Muktagacha upazilla -> black
bar_lists[7].set_color('#000000')

plt.xticks(y_pos, upazillas)

# labels
plt.ylabel('Khana Registration')
plt.title('8 Upazilla\'s Data Collection Report (23rd October to 24th November)')
# plt.title('8 Upazilla\'s Data Collection Report 24th November')


plt.show()
