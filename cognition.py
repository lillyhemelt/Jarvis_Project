from . import actions

def process(user_text, model, tokenizer):
    system_response = actions.execute_task(user_text)
    if system_response != "no system action found.":
        return system_response
    
    print("consulting local neural network...")
    ai_response = model.generate_response(user_text, tokenizer)
    return ai_response