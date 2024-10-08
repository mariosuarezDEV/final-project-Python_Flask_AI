from flask import Flask, jsonify, render_template, redirect, request

from EmotionDetection import emotion_detector as ed

app = Flask("Emotion with Flask and AI")

@app.route("/", methods=["GET"])
def index():
    return "<h1>Hello world</h1>"

@app.route("/emotionDetector", methods=["GET","POST"])
def ai_backend():
    if request.method == "GET":
        return render_template("index.html")
    else:
        text_to_analyse = request.form.get("textToAnalyze")

        if not text_to_analyse:
            return jsonify({
                "error": "Invalid text! Please try again!"
            }), 400
        else:
            response = ed(text_to_analyse)
            print(response)
            if response["dominant_emotion"] == None:
                return jsonify({
                    "error": "Invalid text! Please try again!"
                }),400
            else:
                return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5001, host="0.0.0.0")