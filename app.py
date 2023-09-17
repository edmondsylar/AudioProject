from flask import Flask, request, jsonify
import replicate

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Replicate API!"


# call the replicate/llama70b-v2-chat model with a prompt a parmeter```python
@app.route("/llama-prompt", methods=["POST"])
def prompt():
    data = request.get_json()
    prompt = data["prompt"]

    response = replicate.run(
        "replicate/llama70b-v2-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
        {
            "input": {
                "prompt": prompt,
                "temperature": 0.75,
                "top_p": 1,
                "max_length": 1000,
                "repetition_penalty": 1
            }
        }
    )

    completion = response.join('')
    return completion

@app.route("/query-model", methods=["POST"])
def query_model():
    data = request.get_json()
    prompt = data["prompt"]

    # Run the model using Replicate
    output = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input={"prompt": prompt}
    )

    print(output)
    return "jsonify(output)"

if __name__ == "__main__":
    app.run(debug=True)