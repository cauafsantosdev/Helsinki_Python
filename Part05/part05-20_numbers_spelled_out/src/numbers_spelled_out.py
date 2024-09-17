# Write your solution here

def dict_of_numbers():
    zero = ['zero']
    ints = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    betweens = [i + ('' if j == -1 else '-' + ints[j]) for i in tens for j in range(-1, len(ints))]

    nums = list(range(100))
    words = zero + ints + teens + betweens
    d = {nums[i]: words[i] for i in range(len(nums))}

    return d


if __name__ == "__main__":
    print(dict_of_numbers())