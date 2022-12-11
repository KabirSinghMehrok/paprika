# Some test cases to test out the code
from mainfile import *

test_cases = [
    {
        'name': 'Kabir',
        'branch_year': 'I am currently in 3rd year styding computer science and artificial intelligence at IIITD',
        'cgpa': 'Its around 8',
        'career_field': 'I would love to work in design. Yes, I am considering higher education there',
        'courses': 'I have taken ip, dc, hci, ada, dbms, ddv, iag, tdaf, dmg, ai, ml as of now',
    },

    {
        'name': 'Rashit',
        'branch_year': 'Currently, I am in second year of the college, and studying in csd',
        'cgpa': 'Its around 8',
        'career_field': 'I am considering to pursue software development, but i am not considering higher education',
        'courses': 'Courses I had taken: introduction to programming, digital circuts, ai, ml, ada, dsa, dbms, advanced programming',
    },

    {
        'name': 'Randeep Singh',
        'branch_year': 'I am a fourth year student majoring in computer science and biosciences',
        'cgpa': 'my current cpga is 8',
        'career_field': 'I would like to work in biology and allied field. Yes, I am interested in pursuing higher education oppurtunities in biosciences.',
        'courses': 'Courses I had taken: introduction to programming, ai, ml, foundation of biology, biophysics, mlba',
    },
]

def test():
    for tests in test_cases:
        name = ask_name(tests.get('name'))
        branch, year = ask_branch_year(tests.get('branch_year'))
        cgpa = ask_cgpa(tests.get('cgpa'))
        career, field = ask_career_field(tests.get('career_field'))
        courses = ask_courses(tests.get('courses'))
        print()
        print("Input: ")
        print("{} {} {} {} {} {} {}".format(name, branch, year, cgpa, career, field, courses))

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

if __name__ == '__main__':
    test()