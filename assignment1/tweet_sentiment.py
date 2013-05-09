import sys
import json

def hw():
    afinnfile = open("AFINN-111.txt")
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    output = open("output.txt")
    for line in output:
        j = json.loads(line)
        text = ""
        if ("text" in j) :
            text = j['text']

        count = 0
        for word in text.split(' '):
            if (word in scores) == False:
                continue

            count += scores[word]

        print float(count)


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()

if __name__ == '__main__':
    main()
