import gradio as gr
from transformers import pipeline


model = pipeline("summarization")


def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary


with gr.Interface(predict, "textbox", "text") as interface:
    interface.launch()
