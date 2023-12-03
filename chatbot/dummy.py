from flask import Flask, render_template, request, jsonify
import spacy
import json



nlp = spacy.load("en_core_web_sm")

# Load keywords and responses from the JSON file

with open('demo.json', 'r') as f:
    json_data = json.load(f)

user_input=input("ENTER : ")

# Filter the input for matching keywords and accordingly process the output
def get_matched_responses(user_input):

    matched_responses = []

    keywords = ['evaluate', 'claim', 'insurance', 'policy', 'risk']
    user_input_doc = nlp(user_input)
    user_keywords = sorted([token.lemma_ for token in user_input_doc if token.lemma_ in keywords])
    search_key = ' '.join(user_keywords)
    
    if search_key in json_data:
        matched_responses = [item['question'] for item in json_data[search_key] if 'question' in item]

    #matched_responses = json_data.get(search_key)

    return(matched_responses)


def process_question(selected_question):
    # Search for the selected question in the JSON data
    matched_responses = []

    for key, value in json_data.items():
        for item in value:
            if 'question' in item and item['question'] == selected_question:
                matched_responses.append(item.get('answer', "Sorry, no answer found."))

    print(matched_responses)



arr=get_matched_responses(user_input)
print(arr)
process_question(arr[0])
