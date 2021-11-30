one_point_letters = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
two_point_letters = ["d", "g"]
three_point_letters = ["b", "c", "m", "p"]
four_point_letters = ["f", "h", "v", "w", "y"]
five_point_letters = ["k"]
eight_point_letters = ["j", "x"]
ten_point_letters = ["q", "z"]


def scrabble_calc(word):
    score = 0

    for c in word:
        if c in one_point_letters:
            score += 1
        elif c in two_point_letters:
            score += 2
        elif c in three_point_letters:
            score += 3
        elif c in four_point_letters:
            score += 4
        elif c in five_point_letters:
            score += 5
        elif c in eight_point_letters:
            score += 8
        else:
            score += 10

    return score


print(scrabble_calc(input("Input a word.   ")))

