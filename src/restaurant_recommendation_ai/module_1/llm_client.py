import ollama
import time

def llm_model(system_msg, prompt_txt):
    """
    system_msg: system instruction for the LLM
    prompt_txt: user prompt
    """

    model_id = "llama3.1:8b"

    messages = [
        {
            "role": "system",
            "content": system_msg
        },
        {
            "role": "user",
            "content": prompt_txt
        }
    ]

    response = ollama.chat(
        model=model_id,
        messages=messages
    )

    output_text = response["message"]["content"]

    return output_text


def  safe_llm_call(system_msg, prompt_txt, retries=3) :

    for i in range(retries = 3) :

        try: 
            return llm_model(system_msg , prompt_txt)
        except Exception :

            time.sleep(2) 

    return "Failed after retries"       
