import random


words = []

def load_words():
	global words

	with open("words.txt", "r") as file:
		words.append(file.readlines().split("\n"))


def get_random_word():
	global words

	return words.pop(random.choice(words))


def main():
	while len(words) > 0:



if __name__ == "__main__":
	main()
