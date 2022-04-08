from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random
import transformers
transformers.logging.set_verbosity_error()
print("AI-GPT2");
user_inputB = input("download or exec pretrained model[download/exec]?:")
file_object = open('output.txt', 'a', encoding="utf-8")
if user_inputB == "download":
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    model.save_pretrained("./GPT2")
    tokenizer.save_pretrained("./GPT2")
if user_inputB == "exec":
    model = GPT2LMHeadModel.from_pretrained('./GPT2')
    tokenizer = GPT2Tokenizer.from_pretrained('./GPT2')
    user_input = input("USER:")
n = 0
inputs = tokenizer.encode(user_input, return_tensors='pt')
while(True):
    outputs = model.generate(
    inputs, max_length=42, do_sample=True, temperature=0.5
    )
    string = tokenizer.decode(outputs[0], skip_special_tokens=True)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True).replace(proc, "")
    if text.find(".") > 10 and n == 0:
        print("AI:" + text[0:text.find(".")+1])
        outA = text[0:text.find(".")+1]
        n = 1
    if text.find(".") > 10 and n == 1:
        print("AI:" + text[0:text.find(".")+1])
        outB = text[0:text.find(".")+1]
        break
    if n == 1:
        user_choice = input("Validate[Y/N]:")
        if user_choice == "y" or user_choice == "Y":
            outA = outB
            inputs = tokenizer.encode(outA + "\n" + outB, return_tensors='pt')
