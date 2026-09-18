def get_answer_prompt(context, question):
    return f"""
    You are an intelligent assistant. Based on the context provided, answer the following question:

    Context: {context}

    Question: {question}

    Answer:
    """

def get_context_prompt(context):
    return f"""
    You are an intelligent assistant. Here is some context to help you understand the topic:

    Context: {context}

    Please summarize the key points.
    """