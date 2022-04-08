from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random
import transformers
transformers.logging.set_verbosity_error()
def proc(_input):
    while(True):
        inputs = tokenizer.encode(_input, return_tensors='pt')
        outputs = model.generate(
        inputs, max_length=42, do_sample=True, temperature=0.5
        )
        string = tokenizer.decode(outputs[0], skip_special_tokens=True)
        text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        outB = text[0:text.find(".")+1].replace(_input,"")
        if text.find(".") > 10:
            out = text[:text.find(".")+1].replace(_input,"")
            return out
print("AI-GPT2-choice-adaptation");
user_inputB = input("download or exec pretrained model[download/exec]?:")
if user_inputB == "download":
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    model.save_pretrained("./GPT2")
    tokenizer.save_pretrained("./GPT2")
if user_inputB == "exec":
    model = GPT2LMHeadModel.from_pretrained('./GPT2')
    tokenizer = GPT2Tokenizer.from_pretrained('./GPT2')
_input = input("USER:")
textA = proc(_input)
textB = proc(_input)
while(True):
    print("AI:" + textA[0:textA.find(".")+1].replace(_input,""))
    print("AI:" + textB[0:textB.find(".")+1].replace(_input,""))
    user_choice = input("Validate[y/n]:")
    if user_choice == "n" or user_choice == "N":
        textB = proc(_input)
    if user_choice == "y" or user_choice == "Y":
        textA = textB.replace(_input,"")
        textB = proc(_input)