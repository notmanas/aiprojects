from openai import OpenAI
import os
import streamlit as st

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def append_to_file(string_to_append):
    # Open the file in append mode
    filename = 'output.txt'
    with open(filename, 'a') as file:
        # Write the string to the file
        file.write(string_to_append + '\n')  # Add a newline for better formatting


def get_checker_response(user_input):
    model_answer = ("ChatGPT is an AI chatbot developed by OpenAI that uses the GPT (Generative Pre-trained "
                    "Transformer) language model to engage in human-like conversations. It is designed to understand "
                    "natural language inputs and generate relevant, coherent, and context-aware responses. ChatGPT "
                    "can assist with tasks such as answering questions, providing explanations, brainstorming, "
                    "and more. It powers various applications like chatbots, virtual assistants, and content creation "
                    "tools.")
    prompt = f"""
    As a teacher's assistant, your job is to evaluate student answers based on a `Model Answer` on a scale of 1 to 10.
    Also specify the reason for scoring less or more, in detail. 
    
    Here are reasons why you should be deduction from overall score:
    1. Incorrect information in the answer.
    2. Incorrect grammar/poor English writing skills.
    Model Answer: {model_answer}
    
    Example 1:
    Question: What is ChatGPT in 2 sentences?
    Answer by student: ChatGPT is a brand of instant coffee that uses artificial intelligence to brew the perfect cup by analyzing your taste preferences and adjusting the coffee blend accordingly. It’s revolutionizing the coffee industry with AI-driven caffeine experiences!
    Response: Score: 0/10, Reason: The answer is not relevant because ChatGPT is not an instant coffee. 
    
    Example 2:
    Question: What is ChatGPT in 2 sentences?
    Answer by student: ChatGPT is an advanced conversational AI model created by OpenAI that simulates human-like dialogue. It uses deep learning techniques to understand and generate text based on user inputs, enabling it to answer questions, provide information, and assist with a variety of tasks. ChatGPT is widely used in customer support, content creation, and as a virtual assistant in various applications.
    Response: Score: 10/10, Reason: The answer matches with the model answer to a great extent and is factually correct.
    
    Now, find the score for this answer by a student:
    {user_input}
    
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content


st.title("Answer Checker")
user_input = st.text_area("What is ChatGPT? Answer in 2-3 sentences.")
run_btn = st.button("Run")
if run_btn:
    resp = get_checker_response(user_input=user_input)
    st.code(resp, wrap_lines=True, language=None)
    file_name = 'output.txt'
    append_to_file(string_to_append=resp)
