import sys
import json
import operator

def hw(tweet_file):
    output = open(tweet_file)
    hashtags_total = {}

    for line in output:
        j = json.loads(line)
        hashtags = []
        if ("entities" in j) :
            hashtags = j['entities']['hashtags']

        for hashtag_obj in hashtags:
            hashtag = hashtag_obj["text"]
            if (hashtag in hashtags_total) == False:
                hashtags_total[hashtag] = 0

            hashtags_total[hashtag] +=1.0

    array =  sorted(hashtags_total.iteritems(), key=operator.itemgetter(1))

    array = array[len(array)-10:len(array)]
    i = 9
    while i >= 0:
        print array[i][0], array[i][1]
        i-=1


def lines(fp):
    print str(len(fp.readlines()))

def main():
    hw(sys.argv[1])

if __name__ == '__main__':
    main()
