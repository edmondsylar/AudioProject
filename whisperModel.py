import replicate

def process_audio(audio_file_location):
    output = replicate.run(
        "openai/whisper:91ee9c0c3df30478510ff8c8a3a545add1ad0259ad3a9f78fba57fbc05ee64f7",
        input={"audio": open(audio_file_location, "rb")}
    )
    return output

# # Example usage
# audio_file_location = "recording.wav"
# result = process_audio(audio_file_location)
# print(result)

def ai_support(prompt):
    response = replicate.run(
        "replicate/llama70b-v2-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
        input={"prompt": prompt}
    )
    data = ''.join(list(response))
    return data
