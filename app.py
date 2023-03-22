from transformers import pipeline
import torch
import re
import runpod

def handler(event):
    device = 0 if torch.cuda.is_available() else -1
    model = pipeline('summarization', model="braindao/flan-t5-cnn",device=device)

    # Parse out your arguments
    prompt = event['input'].get('content',None)

    CLEANER = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});|\\r|\\n|\s{2,}')

    # cleaning text beforing feeding to model
    if prompt != None:
        prompt = re.sub(CLEANER, '', prompt)

    if prompt == None:
        return {'message': "No prompt provided"}

    # Run the model
    result = model(prompt)
    return result

runpod.serverless.start({"handler": handler})
