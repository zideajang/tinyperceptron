import re
from rich.console import Console

console = Console()
with open("/home/user/tinyperceptron/data/paul_graham_essay.txt") as file:
    essay = file.read()

print(essay)

single_sentences_list = re.split(r'(?<=[.?!])\s+',essay)
print(f"{len(single_sentences_list)} senteneces were found")

sentences = [{'sentence':x,'index':i} for i,x in enumerate(single_sentences_list)]

console.print(sentences[:3])

def combine_sentences(sentences,buffer_size=1):
    for i in range(len(sentences)):
        combined_sentence = ''
        for j in range(i -buffer_size,i):
            if j >= 0:
                combined_sentence += sentences[j]['sentence'] + ' '
        combined_sentence += sentences[i]['sentence']

        for j in range( i + 1,i + 1 + buffer_size):
            if j < len(sentences):
                combined_sentence += ' ' + sentences[j]['sentence']

        sentences[i]['combined_sentence'] = combined_sentence

    return sentences

sentences = combine_sentences(sentences)
console.print(sentences[:3])