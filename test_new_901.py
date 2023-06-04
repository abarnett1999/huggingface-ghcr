import warnings

warnings.filterwarnings("ignore", category=UserWarning)


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from fastapi.testclient import TestClient

app = FastAPI()
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

client = TestClient(app)


@app.get("/")
async def read_root():
    return {"I love": "MLOPs"}


@app.post("/generate", response_class=HTMLResponse)
async def generate_text(request: Request):
    data = await request.json()
    input_text = data.get("input_text", "")
    encoded_input = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(encoded_input)
    generated_text = tokenizer.decode(output[0])
    html_content = f"<h1>Generated Text</h1><p>{generated_text}</p>"
    return html_content


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"I love": "MLOPs"}


def test_generate_text():
    response = client.post("/generate", json={"input_text": "Hello"})
    assert response.status_code == 200
    assert "<h1>Generated Text</h1>" in response.text


# Run tests
import pytest

test_read_root()
test_generate_text()


# Run tests and generate HTML report
if __name__ == "__main__":
    pytest.main(["-vv", "--html=report.html"])
