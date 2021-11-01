import re


def top_3_words(text):
	text = text.lower()
	wordFrequencies = {}
	for word in re.split('[^a-z\']', text):
		if word == "": continue
		if len(re.findall("[a-z]+", word)) == 0: continue

		try:
			wordFrequencies[word] += 1
		except KeyError:
			wordFrequencies[word] = 1

	output = sorted(list(wordFrequencies.items()), key=lambda x: x[1], reverse=True)[:3]
	return [item[0] for item in output]


print(top_3_words("  '''  "))
