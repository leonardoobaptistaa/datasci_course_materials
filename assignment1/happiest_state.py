import sys
import json

def hw(sent_file, tweet_file):
    afinnfile = open(sent_file)
    output = open(tweet_file)
    scores = {}

    better_state = ""
    better_score = -999999

    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    for line in output:
        j = json.loads(line)
        text = ""
        if ("text" in j) :
            text = j['text']
        geo = {}
        if ("place" in j) and j["place"] != None and j["place"]["country_code"] == "US" and j["place"]["place_type"] == "city":
            geo = j["place"]
        else:
            continue

        state_name = geo["full_name"].replace(" ", "").split(",")[1]


        score = 0
        for word in text.split(' '):
            if (word in scores) == False:
                continue

            score += scores[word]

        if score > better_score:
            score = better_score
            better_state = state_name

    print better_state


def lines(fp):
    print str(len(fp.readlines()))

def main():
    hw(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
