import time

import ollama


def llm_model(system_msg, prompt_txt):
    """
    system_msg: system instruction for the LLM
    prompt_txt: user prompt
    """

    model_id = "llama3.1:8b"

    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": prompt_txt},
    ]

    response = ollama.chat(model=model_id, messages=messages)

    output_text = response["message"]["content"]

    return output_text


def safe_llm_call(system_msg, prompt_txt, retries: int = 3):
    for i in range(retries):
        try:
            return llm_model(system_msg, prompt_txt)
        except Exception as e:  # noqa: BLE001
            print(f"llm call attempt {i + 1} failed: {e}")
            time.sleep(2)
