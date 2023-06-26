from flask import Flask, render_template,jsonify, request
from flask_pymongo import PyMongo


import openai

openai.api_key = "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"



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://sahilsalunkhe544:msssk255@talktogpt.xxn8nbn.mongodb.net/TalkToGpt"
mongo = PyMongo(app)

app = Flask(__name__)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    print(chats)
    return render_template("index.html",myChats= myChats)

@app.route("/api", methods=["GET","POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})  # checking if asked question already exists in database
        print(chat)
        if chat:
            data = {"result": f"{chat['answer']}"}
            return jsonify(data)
        else:
            # response = openai.Completion.create(
            #         model="text-davinci-003",
            #         prompt=question,
            #         temperature=1,
            #         max_tokens=256,
            #         top_p=1,
            #         frequency_penalty=0,
            #         presence_penalty=0
            #         )
            # print(response)
            data = {"result": f"Answer of {question} "} #If its not in database, then we will get the answer from openAI
            mongo.db.chats.insert_one({"question":question, "answer":f"Answer from openAI for {question}"})
            return jsonify(data)
    data = {"result": "Thank you for your kind words! I'm here to assist you, so if you have any more questions or need further help, feel free to ask."}
    return jsonify(data)

app.run(debug=True)