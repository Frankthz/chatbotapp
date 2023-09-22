import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response