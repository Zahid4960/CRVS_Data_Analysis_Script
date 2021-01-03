# essentials libraries
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# array for 8 upazillas
upazilla_array = [
    "Singair",
    "Daudkandi",
    "Sujanagar",
    "Pirgacha",
    "Madhabpur",
    "Dacope",
    "Nalcity",
    "Muktagacha"
]

# array for upazilla_wise_member_registration_array
upazilla_wise_member_registration_array = [
    1320,
    9165,
    4107,
    1039,
    254,
    3874,
    612,
    1817
]

# get indexes of sorted upazilla_wise_member_registration_array
s = np.array(upazilla_wise_member_registration_array)
sort_index = np.argsort(s)

# intitiatize ascending and descending value
ascending = 0
descending = 0

# sor upazilla_wise_member_registration_array in ascending order
# upazilla_wise_member_registration_array.sort(reverse=False)
# ascending = 1
# print(sort_index)

# sor upazilla_wise_member_registration_array in descending order
upazilla_wise_member_registration_array.sort(reverse=True)
descending = 1
# print(sort_index)

# total registered member
total_registered_member = upazilla_wise_member_registration_array[0] +upazilla_wise_member_registration_array[1] + upazilla_wise_member_registration_array [2] + upazilla_wise_member_registration_array [3] + upazilla_wise_member_registration_array [4] + upazilla_wise_member_registration_array [5] + upazilla_wise_member_registration_array [6] + upazilla_wise_member_registration_array [7]
# print(total_registered_member)

if ascending == 1:
    # 8 upazillas list
    upazillas = (
        upazilla_array[sort_index[0]] + "\n" + str(upazilla_wise_member_registration_array[0]),
        upazilla_array[sort_index[1]] + "\n" + str(upazilla_wise_member_registration_array[1]),
        upazilla_array[sort_index[2]] + "\n" + str(upazilla_wise_member_registration_array[2]),
        upazilla_array[sort_index[3]] + "\n" + str(upazilla_wise_member_registration_array[3]),
        upazilla_array[sort_index[4]] + "\n" + str(upazilla_wise_member_registration_array[4]),
        upazilla_array[sort_index[5]] + "\n" + str(upazilla_wise_member_registration_array[5]),
        upazilla_array[sort_index[6]] + "\n" + str(upazilla_wise_member_registration_array[6]),
        upazilla_array[sort_index[7]] + "\n" + str(upazilla_wise_member_registration_array[7])
        )

if descending == 1:
        # 8 upazillas list
        upazillas = (
            upazilla_array[sort_index[7]] + "\n" + str(upazilla_wise_member_registration_array[0]),
            upazilla_array[sort_index[6]] + "\n" + str(upazilla_wise_member_registration_array[1]),
            upazilla_array[sort_index[5]] + "\n" + str(upazilla_wise_member_registration_array[2]),
            upazilla_array[sort_index[4]] + "\n" + str(upazilla_wise_member_registration_array[3]),
            upazilla_array[sort_index[3]] + "\n" + str(upazilla_wise_member_registration_array[4]),
            upazilla_array[sort_index[2]] + "\n" + str(upazilla_wise_member_registration_array[5]),
            upazilla_array[sort_index[1]] + "\n" + str(upazilla_wise_member_registration_array[6]),
            upazilla_array[sort_index[0]] + "\n" + str(upazilla_wise_member_registration_array[7])
            )

y_pos = np.arange(len(upazilla_array))
bar_lists = plt.bar(y_pos, upazilla_wise_member_registration_array)

# set individual colors for individual upazillas
# Singair upazilla -> violet
bar_lists[0].set_color('#EE82EE')

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
plt.ylabel('Member Registration')
plt.title('8 Upazilla\'s Data Collection Report (23rd October 2020 to 2nd January 2021)' + "\n" + "Total Registered Member = " + str(total_registered_member))

plt.show()
