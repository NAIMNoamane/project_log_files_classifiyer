
import re
import ollama



def classify_with_llm(log_msg):

    prompt = f'''Classify the log message into one of these categories: 
    (1) Workflow Error, (2) Deprecation Warning.
    Only return the category name. No preamble.
    Put the category inside <category> </category> tags .
    If you can't figure out a category, use "Unclassified". 
    Log message: {log_msg}'''

    chat_completion = ollama.chat(
        messages=[{"role": "user", "content": prompt}],
        model="deepseek-r1:1.5b",
        
    )

    content = chat_completion.message.content
    match = re.search(r'<category>(.*)<\/category>', content, flags=re.DOTALL)
    category = "Unclassified"
    if match:
        category = match.group(1)

    return category
