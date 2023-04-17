import os
import openai
from dotenv import load_dotenv

# openai textComplete例子：https://platform.openai.com/docs/quickstart/build-your-application

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def index(animal):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(animal),
        temperature=0.6,
    )
    result = response.choices[0].text
    print("result:", result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.
Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )


if __name__ == '__main__':
    index("horse")
