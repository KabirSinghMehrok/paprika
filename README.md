# Paprika: a Personalized Electives Advisory System in Prolog

## Introduction
Paprika is a personalized electives recommendation system built using a Python-based natural language interface designed to enhance the functionality and user experience of the electives advisory system developed in Prolog. This interface allows users to provide inputs in human language, which are then processed and utilized by the Prolog program. The goal is to create an effective and engaging interface while maintaining simplicity.

## Installation
To run Paprika, follow these steps:
1. Navigate to the project folder.
2. Install the required dependencies by executing the following command:
   ```
   pip install -r requirements.txt
   ```
   Note: Make sure you have Python and pip installed on your system.
3. Run the program by executing the following command:
   ```
   python3 mainfile.py
   ```

## Program Structure

### Electives Advisory System
Paprika considers various factors such as the student's name, branch, year, career goals, field of interest, completion of a BTP (Bachelor Thesis Project), and a list of courses already taken.
- Using advanced techniques such as recursion, backtracking, variable binding, and list operations, the system suggests a tailored list of courses that the student can consider. The knowledge base stores a list of recommended courses for specific fields and their prerequisites.
- The main technical components of this system include capturing user inputs, processing and analyzing the data, leveraging recursion and backtracking algorithms to generate course suggestions, and utilizing a knowledge base to store course recommendations and prerequisites.

### NLP pipeline
Paprika incorporates a natural language processing pipeline, leveraging the Natural Language Toolkit (NLTK), to extract meaningful information from user input. The pipeline processes the natural language input and generates a list of root words. These root words are then searched for keywords relevant to the specified search space. The structure of the natural language processing pipeline is as follows:

1. Tokenization: The input text is divided into individual tokens.
2. Root Word Extraction: The pipeline identifies the root words of the tokens, enabling a better understanding of the user's intent.
3. Keyword Identification: The pipeline searches for specific keywords related to the electives advisory system within the root words.
4. Integration with Prolog: The extracted information is then utilized by the Prolog program via pyswip, enabling the advisory system to generate personalized elective recommendations.

<div align="center">
	<img src="https://i.imgur.com/x8TKRaS.png">
    <p><i>Figure: Structure of the natural language pipeline used</i></p>
</div>

Note: The system assumes the student is in the 3rd year or above, as the advised courses are typically available to students during the 3rd and 4th years.


