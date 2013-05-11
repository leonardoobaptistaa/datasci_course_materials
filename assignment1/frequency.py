import sys
import json

def main():
    
    output = open(sys.argv[1])
    total_terms = 0
    terms_count = {}

    for line in output:
        j = json.loads(line)
        text = ""
        if ("text" in j):
            text = j['text']

        for word in text.split(' '):

            word = word.encode('utf-8').replace("\n", "")
            if (word in terms_count) == False:
                terms_count[word] = 0

            terms_count[word]+=1.0
            total_terms+=1.0

    for word in terms_count.keys():
        #print word.encode('utf-8'), "{0:.30f}".format(terms_count[word]/total_terms)
        print "%s %f" % (word, terms_count[word]/total_terms)


if __name__ == '__main__':
    main()
