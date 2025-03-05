from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv

# Retrieve the open AI key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=openai_api_key)
openai = OpenAI(
    api_key = openai_api_key
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') #Calls the index html

@app.route("/ask", methods = ['POST'])
def ask():
    user_message = request.form.get("user_input")  # This is what the user asks

    # Open AI response
    response = openai.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": "respond to the user as a chatbot."},
            {"role": "user", "content": user_message}
        ]
    )

    print(response)
    openai_response = response.choices[0].message['content']  # Get the response

    return render_template('index.html', user_message=user_message, openai_response=openai_response)  # Pass it to the frontend


if __name__ == '__main__':
    app.run(debug=True)