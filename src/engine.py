from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, PhiConfig
import gradio as gr
import fitz  # PyMuPDF
import torch

# --- CONFIGURATION ---
HF_USERNAME = "hobbesthecomputerscientist"
MODEL_ID = f"{HF_USERNAME}/mock-trial-ai-v2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
config = PhiConfig.from_pretrained(MODEL_ID, trust_remote_code=True)
config.model_type = "phi"
if not hasattr(config, "pad_token_id") or config.pad_token_id is None:
    config.pad_token_id = tokenizer.eos_token_id if tokenizer.eos_token_id else 50256

model = AutoModelForCausalLM.from_pretrained(MODEL_ID, config=config, trust_remote_code=True, dtype=torch.float16, device_map="auto")
tokenizer.pad_token = tokenizer.eos_token
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# --- UTILS ---

def clean_ai_response(text):
    """Cuts off hallucinations while allowing for longer legal explanations."""
    stop_words = ["Illustration", "Example", "Exercise", "### Instruction", "Scenario", "Note:", "Discussion"]
    for word in stop_words:
        if word in text: text = text.split(word)[0]
    return text.strip()

def extract_pdf_text(pdf_file):
    if pdf_file is None: return ""
    text = ""
    path = pdf_file.name if hasattr(pdf_file, 'name') else pdf_file
    with fitz.open(path) as doc:
        for page in doc: text += page.get_text()
    return text[:4500]

# --- MODE LOGIC ---

def mock_trial_engine(pdf, mode, name, exam_type, user_input):
    case_text = extract_pdf_text(pdf) if pdf else "No PDF provided."

    if mode == "🎭 Witness Simulator":
        # Force the AI to stay in persona and be defensive
        instruction = (
            f"You are the witness {name}. ROLE: {exam_type}. "
            f"STRICT RULES: Use ONLY the provided case facts. If asked a trick question or a lie, "
            f"deny it firmly based on the text. Do not agree with the attorney. "
            f"TEXT: {case_text}"
        )
        temp, rep_pen = 0.2, 1.2

    elif mode == "⚖️ Objection Checker":
        # Standalone Judge logic
        instruction = (
            "You are a HIGH COURT JUDGE. Your only job is to rule on the input question. "
            "Is it Leading? Hearsay? Speculation? Relevance? Answer with: "
            "'RULING: [Objection Type] - REASONING: [Legal Explanation]' "
            "DO NOT answer the question as a witness."
        )
        temp, rep_pen = 0.01, 1.1

    elif mode == "🎯 Objection Practice":
        # Generate a question to test the user
        instruction = (
            f"Generate a realistic courtroom question for the witness {name}. "
            "The question should be intentionally flawed (Leading or Hearsay) to test a student. "
            f"CASE CONTEXT: {case_text}"
        )
        temp, rep_pen = 0.7, 1.0

    else: # Case Analysis
        instruction = f"Provide a detailed strategic analysis of the case packet: {case_text}"
        temp, rep_pen = 0.3, 1.1

    prompt = f"### Instruction:\n{instruction}\n\n### Input:\n{user_input}\n\n### Response:"
    res = generator(prompt, max_new_tokens=300, do_sample=(temp > 0), temperature=max(temp, 0.01), repetition_penalty=rep_pen)
    return clean_ai_response(res[0]['generated_text'].split("### Response:")[-1])

def solve_practice(pdf, question, guess):
    case_text = extract_pdf_text(pdf)
    # The 'Coach' prompt: compares guess to the actual question
    instruction = (
        f"The question asked was: '{question}'. The student's objection was: '{guess}'. "
        "Explain if the student is correct. Define the legal rule (Leading/Hearsay/etc.) "
        f"and cite if the question violates it based on: {case_text}"
    )
    prompt = f"### Instruction:\n{instruction}\n\n### Input:\nEvaluate the ruling.\n\n### Response:"
    res = generator(prompt, max_new_tokens=250, do_sample=False, repetition_penalty=1.2)
    return clean_ai_response(res[0]['generated_text'].split("### Response:")[-1])

# --- UI (Improved Layout) ---

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🏛️ Mock Trial AI")

    with gr.Tab("🎯 Objection Practice"):
        op_pdf = gr.File(label="Upload Case Packet")
        op_name = gr.Textbox(label="Witness to Question")
        gen_btn = gr.Button("Generate Attorney Question")
        generated_q = gr.Textbox(label="AI Attorney Question:", lines=2)

        user_choice = gr.Radio(["No Objection", "Leading", "Hearsay", "Speculation", "Relevance", "Argumentative"], label="Your Objection Choice")
        solve_btn = gr.Button("Submit Ruling", variant="primary")
        explanation = gr.Textbox(label="Judge's Feedback", lines=6)

        gen_btn.click(fn=lambda p,n: mock_trial_engine(p,"🎯 Objection Practice",n,"","Give me a question."), inputs=[op_pdf, op_name], outputs=[generated_q])
        solve_btn.click(solve_practice, inputs=[op_pdf, generated_q, user_choice], outputs=explanation)

    with gr.Tab("⚖️ Objection Checker"):
        gr.Markdown("Input a question here to see if it is objectionable. No PDF required.")
        oc_input = gr.Textbox(label="Question to Rule On", placeholder="e.g. You saw him do it, didn't you?")
        oc_btn = gr.Button("Judge's Ruling", variant="primary")
        oc_output = gr.Textbox(label="Rulings & Reasoning", lines=5)
        oc_btn.click(fn=lambda i: mock_trial_engine(None,"⚖️ Objection Checker","","",i), inputs=oc_input, outputs=oc_output)

    with gr.Tab("🎭 Witness Simulator"):
        with gr.Row():
            ws_pdf = gr.File(label="Upload PDF")
            with gr.Column():
                ws_name = gr.Textbox(label="Witness")
                ws_type = gr.Radio(["Direct", "Cross"], label="Mode", value="Cross")
        ws_input = gr.Textbox(label="Attorney Question")
        ws_btn = gr.Button("Question Witness")
        ws_output = gr.Textbox(label="Response")
        ws_btn.click(fn=lambda p,n,t,i: mock_trial_engine(p,"🎭 Witness Simulator",n,t,i), inputs=[ws_pdf, ws_name, ws_type, ws_input], outputs=ws_output)

    with gr.Tab("📋 Case Analysis"):
        ca_pdf = gr.File(label="Upload PDF")
        ca_input = gr.Textbox(label="Analysis Query")
        ca_btn = gr.Button("Execute Analysis")
        ca_output = gr.Textbox(label="Strategic Breakdown")
        ca_btn.click(fn=lambda p,i: mock_trial_engine(p,"📋 Case Analysis","","",i), inputs=[ca_pdf, ca_input], outputs=ca_output)

if __name__ == "__main__":
    demo.launch(share=True)
