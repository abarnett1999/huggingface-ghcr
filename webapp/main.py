# from transformers import pipeline
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel

# generator = pipeline('text-generation', model='gpt2')

# app = FastAPI()


# class Body(BaseModel):
#     text: str


# @app.get('/')
# def root():
#     return HTMLResponse("<h1>A self-documenting API to interact with a GPT2 model and generate text</h1>")


# @app.post('/generate')
# def predict(body: Body):
#     results = generator(body.text, max_length=35, num_return_sequences=1)
#     return results[0]

# from fastapi import FastAPI, Request
# from transformers import GPT2Tokenizer, GPT2Model
# from fastapi.responses import HTMLResponse


# app = FastAPI()

# # Load Hugging Face GPT-2 model and tokenizer
# model_name = "gpt2"
# model = GPT2Model.from_pretrained(model_name)
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)


# @app.post("/generate", response_class=HTMLResponse)
# async def generate_text_post(request: Request):
#     input_data = await request.json()
#     input_text = input_data["input_text"]

#     # Generate text using Hugging Face GPT-2 model
#     encoded_input = tokenizer.encode(input_text, return_tensors="pt")
#     output = model.generate(encoded_input)
#     generated_text = tokenizer.decode(output[0])
#     # Format generated text as HTML
#     html_content = generate_html(generated_text)

#     return html_content


# @app.get("/generate", response_class=HTMLResponse)
# async def generate_text_get(input_text: str):
#     # Generate text using Hugging Face GPT-2 model
#     encoded_input = tokenizer.encode(input_text, return_tensors="pt")
#     output = model.generate(encoded_input)
#     generated_text = "Replace me by any text you'd like."
#     generated_text = tokenizer.decode(output[0])
#     # Format generated text as HTML
#     html_content = generate_html(generated_text)

#     return html_content


# def generate_html(text):
#     html_content = f"<h1>Generated Text</h1><p>{text}</p>"
#     return html_content

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from transformers import GPT2Tokenizer, GPT2LMHeadModel

app = FastAPI()
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/generate", response_class=HTMLResponse)
async def generate_text(request: Request):
    data = await request.json()
    input_text = data.get("input_text", "")
    encoded_input = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(encoded_input)
    generated_text = tokenizer.decode(output[0])
    html_content = f"<h1>Generated Text</h1><p>{generated_text}</p>"
    return html_content
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
