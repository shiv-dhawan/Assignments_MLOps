### Binary didgits to decimal, binary, octal and hexadecimal values.

n = [0,1,1,0,1,1,0]
d = sum(val*(2**idx) for idx, val in enumerate(reversed(n)))
print("The decimal representation of 0110110 :", d)
b = str(bin(d))
print("The binary representation of 0110110 :",b[2:])
o = str(oct(d))
print("The octal representation of 0110110 :",o[2:])
h = str(hex(d))
print("The hexadecimal representation of 0110110 :",h[2:])

### Longest working slot.

from string import ascii_lowercase
input = [[0, 1], [0, 3], [4, 5], [5, 6], [4, 10]]
dict_map = {v:k for k,v in enumerate(ascii_lowercase)}
def get_keys_from_value(d, val):
    key = [k for k, v in d.items() if v == val]
    return str(''.join(key))
# print(get_keys_from_value(dict_map, 0))

def task(input_list):
    t1=0;
    t2=0;
    ind = []
    time_taken = []
    for i in input_list:
        ind.append(i[0])
        t2 = i[1] - t1;
        time_taken.append(t2)
        t1 = i[1]
    max_time = time_taken.index(max(time_taken))
    max_ind = ind[max_time]
    return print("The longest working slot is of :",get_keys_from_value(dict_map, max_ind))
task(input)

### Longest consecutive 1's in binary

def find_max_ones(num):
    if not num:
        return 0
    bin_num = bin(num)[2:]
    print(bin_num)
    return len(max(bin_num.replace('0', ' ').split(), key=len))

print(find_max_ones(44))

from itertools import groupby
def ask_user(message="", type_=str):
    while True:
        try:
            return type_(input(message))
        except ValueError:
            print("wrong type, try again")

def to_binary(x):
    return format(x, "b")

def longest_run_of(it, value):
    return max(len(list(group))
               for c, group in groupby(it)
               if c == value)

if __name__ == "__main__":
    n = ask_user("Enter a number: ", int)
    n_bin = to_binary(n)
    longest_run = longest_run_of(n_bin, "1")
    print(f"count is = {longest_run}")
# print(longest_run_of('101111011101111', '1'))