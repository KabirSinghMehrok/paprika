
import nltk
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import *
import regex as re
from pyswip import Prolog

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('universal_tagset', quiet=True)

# **NLP Pipeline**
# 
# Data Cleaning
# - Removing extra spaces
# - Removing puncutations and other unecessary characters
# - Case normalization
# - Tokenization
# - Removing stopwords
# - Dealing with numbers
# 
# Stemming/Lemmatization
# 
# *POS

stopwords_list = stopwords.words('english')
stopwords_list.remove('no')
stopwords_list.remove('not')

word_number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
ordinal_number = ['zeroth', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

branches = {
'artifici': 'csai',
'intellig': 'csai',
'mathemat': 'csam',
'bioscienc': 'csb',
'design': 'csd',
'engin': 'cse',
'electron': 'ece',
'commun': 'ece',
'social': 'csss',
'csb': 'csb',
'cse': 'cse',
'csd': 'csd',
'csai': 'csai',
'csss': 'csss',
'ece': 'ece',
}

careers_dict = {
    'design': 'desi',
    'development': 'sdev',
    'cyber': 'cysc',
    'security': 'cysc',
    'cybersecurity': 'cysc',
    'biology': 'biol',
    'biotechnology': 'biol',
    'machine ': 'aiml',
    'mathematics': 'math',
    'artificial': 'aiml',
    'economics': 'econ',
    'intelligence': 'aiml',
    'data': 'data',
    'software': 'sdev',
    'ml': 'aiml',
    'ai': 'aiml',
}

courses_list = ['cldc', 'chi', 'nb', 'dmg', 'ml', 'ac', 'gt', 'ra', 'ita', 'df', 'sc', 'ff', 'dsa', 'tdaf', 'cmpa', 'fcs', 'ada', 'nlp', 'davp', 'mlba', 'ra2', 'iag', 'mad', 'ip', 'biop', 'dpm', 'efd', 'tnt', 'cn', 'm3', 'dm', 'spa', 'ai', 'vdc']
courses_dict = {
'structures' : 'dsa',
'management' : 'dpm',
'cryptography': 'ac', 
'futures': 'df', 
'natural': 'nlp', 
'visual': 'vdc',
'stochastic': 'spa', 
'complex': 'cmpa', 
'scientific': 'sc', 
'biophyscis' : 'biop', 
'modern' : 'mad', 
'audio' : 'davp', 
'cheminformatics' : 'chi', 
'discrete' : 'dm', 
'ergonomics' : 'efd', 
'graphics' : 'iag', 
'programming' : 'ip', 
'number' : 'tnt', 
'cloud' : 'cldc', 
'finance' : 'ff', 
'real' : 'ra', 
'artificial' : 'ai', 
'advanced' : 'ada', 
'maths' : 'm3', 
'data mining' : 'dmg', 
'film' : 'tdaf', 
'transform' : 'ita', 
'machine' : 'ml', 
'biomedical' : 'mlba', 
'network' : 'nb', 
'security' : 'fcs', 
'computer' : 'cn', 
'game' : 'gt', 
}




def text_clean(inp):
    out = inp

    # removing extra spaces
    out = re.sub("\s+"," ", out)

    #removing punctuations and other characters
    out = re.sub("[^0-9A-Za-z ]", "" , out)

    #case normalization
    out = out.lower()

    # tokenization
    out = word_tokenize(out)

    # removing stopwords and non-sense words
    out = [word for word in out if word not in stopwords_list]

    # Dealing with numeric words and numbers
    # first we need to convert positional numbers to simple number
    # iterate over list, if any string has starting digit, extract it
    for word in out[:]:
        if word[0].isnumeric() and len(word) != 1:
            out.append(word[0:1])
            out.remove(word)

    # convert any word number into simple number
    for word in out[:]:
        if word in word_number:
            out.append(str(word_number.index(word)))
            out.remove(word)
        if word in ordinal_number:
            out.append(str(ordinal_number.index(word)))
            out.remove(word)
    
    # make unique list
    out = list(set(out)) 

    return out

def stem(inp):
    out = inp
    ps = PorterStemmer()
    out = [ps.stem(word) for word in out]

    # make unique list
    out = list(set(out))

    return out

def ask_name(inp):
    # print(out)
    name = inp.split()[0]
    # find the name
    # tagged = pos_tag(out)
    # print(tagged)
    # name = next(tup[0] for tup in tagged if tup[1] == 'NNP')
    return name

def ask_branch_year(inp):
    branch = False
    year = False
    out = stem(text_clean(inp))
    # print(out)

    for word in out:
        # get information about both branch and year
        if word in branches.keys():
            branch = branches.get(word)
        if word.isnumeric():
            year = word
        
        # when i have information about both year and branch, break
        if branch and year:
            break
    
    if not branch:
        print("I wonder if you have entered your branch name correctly, please try once more")
        return False
    if not year:
        print("It seems like you forgot to give information about your year of study. Can you tell me once more?")
        return False
    
    return [branch, year]

def ask_cgpa(inp):
    # CGPA = False
    out = stem(text_clean(inp))
    # for word in out:
    #     if word.isnumeric():
    #         CGPA = word
    #         break
    CGPA = next(word for word in out if word.isnumeric())

    return CGPA

def ask_career_field(inp):
    career = False
    field = False
    out = text_clean(inp)
    # print(out)
    
    # checking for occurance of anything related to given careers
    for word in out:
        if word in careers_dict.keys():
            career = careers_dict.get(word)
            break
    # checking if user agrees to higher education
    if 'yes' in out or 'yeah' in out:
        field = 'hiedu'
    if 'no' in out or 'not' in out:
        field = 'indst'
    
    if not career:
        print("Seems like the career you have chosen is out of the scope of my advice. Do you have any alternatives on your mind?")
        return False
    if not field:
        print("You haven't talked about if you are interested in higher education or not!")
        return False

    return [career, field]

def ask_courses(inp):
    courses_taken = []
    out = text_clean(inp)
    # print(out)
    for word in out:
        if word in courses_dict.keys():
            courses_taken.append(courses_dict.get(word))
        elif word in courses_list:
            courses_taken.append(word)
    courses_taken = list(set(courses_taken))
    courses_taken_string = '['
    for i in range(len(courses_taken)-1):
        courses_taken_string += courses_taken[i] + ", "
    courses_taken_string += courses_taken[len(courses_taken)-1] + ']'
    return courses_taken_string

def main():
    print('----------------------------------------------')
    print('''
 ____   __    ____  ____  ____  _  _    __   
(  _ \ /__\  (  _ \(  _ \(_  _)( )/ )  /__\  
 )___//(__)\  )___/ )   / _)(_  )  (  /(__)\ 
(__) (__)(__)(__)  (_)\_)(____)(_)\_)(__)(__)
    ''')
    print('------ By Kabir Singh Mehrok, 2020382  -------')
    print()
    print("Hey there! I'm Paprika,  and I am here to make your college life easier!")
    print("What is your name?")
    name = ask_name(input("> "))
    print("Nice to meet you, {}".format(name.title()))
    # print("Inp: " + name)
    print()
    print("What is your current branch and in which year are you studying? It will help me narrow down the list of courses for you")
    branch, year = ask_branch_year(input("> "))
    # print("Inp: " + branch)
    # print("Inp: " + year)
    print()
    print("What is your current CGPA? Tell me the nearest integer value.")
    cgpa = ask_cgpa(input("> "))
    # print("Inp: " + cgpa)
    print()
    print("After graduating from this college, what is the most likely field that you would like to work into? Also, are you also considering higher education in your chosen field?")
    career, field = ask_career_field(input("> "))
    # print("Inp: " + career)
    # print("Inp: " + field)
    print()
    print("Great! I would like to know about what all courses that you have undertaken till now at IIIT Dellhi?")
    courses = ask_courses(input("> "))
    # print("Inp: " + courses)
    print()
    print("Thanks for all that input from your side. Here is the final list of courses (in course code format) that you can take up! : ")

    # prolog processing
    prolog = Prolog()
    prolog.consult("ass1.pl")
    prolog.assertz("name({})".format(name))
    prolog.assertz("branch({})".format(branch))
    prolog.assertz("year({})".format(year))
    prolog.assertz("career({})".format(career))
    prolog.assertz("field({})".format(field))
    prolog.assertz("cgpa({})".format(cgpa))
    prolog.assertz("done({})".format(courses))

    result = list(prolog.query("analyse."))
    # result = list(prolog.query(("final(X)")))

    if (len(result) == 0):
        exit()
    
if __name__ == '__main__':
    main()