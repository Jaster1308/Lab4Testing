# New camelcase program for unit testing


def main():

    sentence = get_input()
    camelcased = camelcase_word(sentence)
    print(camelcased)

    if not valid_sentence(sentence):
        print("Can't process this input")
        return

    words = split(sentence)

    method_name = ""

    first_word = False

    for word in words:

        if not first_word:
            cameling = first_word_done(word)
            first_word = True

        else:
            cameling = camelcase_word(word)

        method_name += cameling

    display_output(method_name)

def get_input():
    return input("Enter sentence: ")

def valid_sentence(sentence):
    return True

def display_output(output):
    print(output)

def split(words):
    return words.split()

def first_word_done(word):
    return word.lower()

def camelcase_word(word):
    inlowercase = word.lower()
    firstletter = word[0]
    firstletter = firstletter.upper()
    rest_word = inlowercase[1:]

    camelcased = firstletter + rest_word

    return camelcased

if '__name__' == '__main__':
    main()