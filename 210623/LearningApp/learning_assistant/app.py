from flask import Flask, render_template, request, redirect, url_for , jsonify
import json
import utils
import os
# from gensim.models import KeyedVectors


app = Flask(__name__)

glove_file = 'data/embeddings/glove.6B.300d.txt'
tmp_file = 'data/embeddings/word2vec-glove.6B.300d.txt'
model = None

if os.path.isfile(glove_file):
    from gensim.scripts.glove2word2vec import glove2word2vec
    glove2word2vec(glove_file, tmp_file)
    model = KeyedVectors.load_word2vec_format(tmp_file)
else:
    print("Glove embeddings not found. Please download and place them in the following path: " + glove_file)

global answers
global quiz_data_v2
global questionText
questionText = ""

with open("details.json", "r") as jf:
    data = json.load(jf)
    users = data["login"]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form.get('login-email')
        password = request.form.get('login-password')

        # Do something with the form data (e.g., authentication)
        if email in users.keys() and users[email]==password:
            # Redirect to generate_qna.html
            return redirect(url_for('generate_qna'))

    return render_template('auth.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form.get('signup-email')
        password = request.form.get('signup-password')
        password2 = request.form.get('confirm-signup-password')

        # Perform validation or other actions with the form data
        with open("details.json", "w") as jfk:
            users[email] = password
            json.dump(users, jfk)
       
        # Print form data (for demonstration purposes)
        print(f'Email: {email}, Password: {password} ,  password2 : { password2}')
        
        # Add your logic for user registration or other actions
        return redirect(url_for('login'))

    return render_template('auth.html')




@app.route('/create_post' , methods=['GET', 'POST'] )
def create_post():
    # Additional logic for generating Q&A or render a template
     if request.method == 'POST':
            # Retrieve form data
        new_post = request.form.get('post-input')
       

        # Perform validation or other actions with the form data
       
        # Print form data (for demonstration purposes)
        print(f'new_post: {new_post}')
        return redirect(url_for('forum'))
    



@app.route('/generate_qna' , methods=['GET', 'POST'])
def generate_qna():
    # Additional logic for generating Q&A or render a template
    question_data = [
    {"subject": "Math", "num_questions": 10},
    {"subject": "Science", "num_questions": 10},
    {"subject": "Python", "num_questions": 10},
    {"subject": "Networks", "num_questions": 10},
    # Add more data as needed
]

    return render_template('generate_qna.html' , questions=question_data)


@app.route('/answer_evaluation')
def answer_evaluation():
    subj_data = data["scores"]
    subjects_data = [
        {"subject": list(subj_data.keys())[0], "score": subj_data[list(subj_data.keys())[0]]},
        {"subject": list(subj_data.keys())[1], "score": subj_data[list(subj_data.keys())[1]]},
        {"subject": list(subj_data.keys())[2], "score": subj_data[list(subj_data.keys())[2]]},
    ]

    return render_template('answer_evaluation.html', subjects_data=subjects_data)
    # Additional logic for generating Q&A or render a template
  


@app.route('/forum')
def forum():
    # Additional logic for generating Q&A or render a template
    return render_template('forum.html')


@app.route('/quiz' , methods=['GET', 'POST'])
def quiz():
    global answers
    global quiz_data_v2
    global questionText
    quiz_data = [

    {
        "question": "For Fiscal year 2021, what was your total GhG Carbon Emission for all scopes?",
        "distractors": [
            "Scope 1 - Determine environmental impact levels.",
            "Scope 2 - Reduce carbon footprints.",
            "Scope 3 - Enhance environmental impacts on a larger scale.",
            "I do not know the answer to this question.",
        ],
    },
    {
        "question": "Another question?",
        "distractors": [
            "Option 1",
            "Option 2",
            "Option 3",
            "I do not know the answer to this question.",
        ],
    },


    # Add more questions and answers as needed
    ]
    if request.method == 'POST':
        print("post method ************")
        questionText = request.form.get('questionText')
        print(f"Launching quiz for subject: {questionText}")
        quiz_data = utils.generateQuestions(questionText, 10, model=model)

        quiz_data_v2 = []
        answers = []
        for item in quiz_data:
            # d = ast.literal_eval(item)
            js_data = {
                "question": item['question'],
                "answers": [item['answer']]+item['distractors'][1:]
            }
            quiz_data_v2.append(js_data)
            answers.append(item['answer'])
        print(quiz_data_v2)
        print("Answers:", answers)

        # return redirect(url_for('quiz'))
        render_template('quiz.html' , quiz_data=quiz_data_v2)
    
    return render_template('quiz.html', quiz_data=quiz_data_v2)
            



@app.route('/quiz/respnse', methods=['GET', 'POST'])
def quiz_response():
    if request.method == 'POST':
        # Form data submitted, process it
        question = request.form.getlist('question')
        selected_answers = request.form.getlist('selected-answer')
        # Do something with selected_answers

        score = 0
        for i in range(len(answers)):
            if answers[i]==selected_answers[i]:
                score += 1

        # For now, just print the selected answers
        print("Question:", question)
        print("Selected Answers:", selected_answers)
        result = "fail" if score<5 else "pass"
        # You can redirect to a different page or render a new template
        return render_template('quiz.html', result=result)

    # If it's a GET request, render the quiz form
    # return render_template('quiz.html', quiz_data=quiz_data)

        

@app.route('/logout')
def logout():
    # Additional logic for generating Q&A or render a template
    return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=False)
