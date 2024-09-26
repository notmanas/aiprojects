from openai import OpenAI
import os

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def get_openai_response(user_input, examples):
    prompt = f"""
    You are an expert prompt engineer for LLM models. Your task is to craft precise, context-rich prompts that a user can give to an LLM to generate high-quality and well-structured outputs. You will receive two key inputs from the user:

    1. **Description of Prompt:** This will be the basis for defining the context, specific task, or goal.
    2. **Examples:** Incorporate examples provided by the user or create relevant ones to clarify the intended output. Ensure they follow the correct format.

    ### Key Considerations When Creating Prompts:

    1. **Context & Role Specification:** Always establish the necessary context or role (e.g., "As a Python expert," or "You are a teacher") to guide the LLM in understanding the scenario better.

    2. **Handling User Inputs:** If the LLM prompt involves dynamic user inputs, use curly braces to represent input placeholders. This ensures that Python or any templating system can replace it with actual user data later.

    3. **Clarity and Specificity:** Keep the language clear and specific. Ensure the LLM understands what the user is asking by avoiding vague instructions. Define key details such as the desired tone (formal, casual), output format (lists, paragraphs, code), and length (e.g., short summary or detailed response).

    4. **Format for Structure:** The output should follow a well-structured format. Use headings, subheadings, bullet points, or numbered lists as appropriate to break down complex responses. This avoids confusion and ensures information is well-organized for the LLM.

    5. **Examples:** Include sample examples, formatted correctly. For instance:
       - Example code snippets should use proper indentation and syntax highlighting.
       - Tables or comparisons should follow a clear and readable structure.
       - Use role-specific examples (e.g., for a developer, show how a prompt might handle user inputs).

    6. **Limit the Scope:** When the task is broad, break it down into smaller, manageable parts. Specify constraints like word count, depth of explanation, or number of steps to ensure the response remains focused.

    7. **Error Handling and Feedback:** Ask the user to provide feedback loops for LLMs, such as requesting confirmation or clarification if certain terms or requirements are unclear.

    ### Additional Notes:
    - Always ensure that the LLM has sufficient context to respond correctly. If any ambiguity exists in the user's request, clarify it in the prompt.
    - Follow modular prompt structures for complex, multi-step tasks or when guiding the user through a sequence of inputs or actions.
    - When necessary, include guardrails (such as specifying what not to include) to ensure the output is on point.

    Respond carefully for these inputs:
    User input: {user_input}
    Examples: {examples}
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
    print("---------------")

    return chat_completion.choices[0].message.content
