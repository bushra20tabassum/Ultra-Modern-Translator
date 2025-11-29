from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        text = data.get("text")
        source = data.get("source")
        target = data.get("target")

        # Fix: GoogleTranslator fails when source="auto"
        if source == "auto":
            source = "auto"   # deep_translator supports this

        translated = GoogleTranslator(source=source, target=target).translate(text)

        return jsonify({"translated": translated})

    except Exception as e:
        print("ERROR:", e)  # Debugging output in terminal
        return jsonify({"error": "Translation failed. Please try again."}), 500


if __name__ == "__main__":
    app.run(debug=True)
