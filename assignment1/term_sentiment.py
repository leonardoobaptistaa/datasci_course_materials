import sys
import json

def main():
    
    afinnfile = open(sys.argv[1])
    output = open(sys.argv[2])
    scores = {}
    new_scores = {}

    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    for line in output:
        j = json.loads(line)
        text = ""
        if ("text" in j):
            text = j['text']

        text_score = 0
        for word in text.split(' '):
            if (word in scores) == False:
                continue

            text_score += scores[word]

        for word in text.split(' '):
            if (word in scores) == True:
                continue

            if (word in new_scores) == False:
                new_scores[word] = 0

            new_scores[word] += text_score

    for word in new_scores.keys():
            print word, float(new_scores[word])


if __name__ == '__main__':
    main()
