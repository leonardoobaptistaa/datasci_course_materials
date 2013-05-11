import sys
import json

def hw(sent_file, tweet_file):
    afinnfile = open(sent_file)
    output = open(tweet_file)
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)

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
    hw(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
