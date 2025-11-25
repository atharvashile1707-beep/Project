from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("f.html") # 1st Page

@app.route("/f")
def f_page():
    return render_template("index.html") # 2nd Page

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    name = request.form.get("name")
    email = request.form.get("email")
    rating = request.form.get("rating")
    message = request.form.get("message")

    with open("feedback.txt", "a") as f:
        f.write(
            f"Name: {name}\nEmail: {email}\nRating: {rating}\nFeedback: {message}\n----------------------\n"
        )

    return f"""
    <h2>Thank you {name}!</h2>
    <p>Your feedback has been successfully submitted.</p>
    <a href="/">Go Back to Home Page</a>
    """

correct_answers = {
    "q1": "a",
    "q2": "b",
    "q3": "a",
    "q4": "a",
    "q5": "b",
    "q6": "c",
    "q7": "a",
    "q8": "c",
    "q9": "b",
    "q10": "b",
    "q11": "a"
     }

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

@app.route('/check_quiz', methods=['POST'])
def check_quiz():
    score = 0
    user_answers = {}

    for q in correct_answers:
        user_choice = request.form.get(q)
        user_answers[q] = user_choice

        if user_choice == correct_answers[q]:
            score += 1

    return render_template(
        "result.html",
        score=score,
        user_answers=user_answers,
        correct_answers=correct_answers
    )

if __name__ == "__main__":
    app.run(debug=True)

