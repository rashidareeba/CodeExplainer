import os
import gradio as gr
from dotenv import load_dotenv
import requests

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

SUPPORTED_MODELS = ["llama-3.3-70b-versatile", "llama2-70b-4096"]

def explain_code(code, expertise_level="beginner", model="llama-3.3-70b-versatile"):
    if not code.strip():
        return "Error: Please enter some code to explain"
    
    if model not in SUPPORTED_MODELS:
        return f"Error: Unsupported model {model}"

    try:
        system_message = {
            "beginner": "Explain this code simply for new programmers. Avoid jargon. Focus on basic concepts and what the code does overall.",
            "expert": "Provide technical analysis for experienced developers. Include optimization ideas, edge cases, and complexity assessment."
        }[expertise_level]

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"Explain this code:\n\n{code}"}
            ],
            "temperature": 0.3
        }

        response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=20)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
        
    except requests.exceptions.HTTPError as e:
        return f"API Error: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

with gr.Blocks(title="Code Explainer", theme="soft") as demo:
    gr.Markdown("""
    # 🚀 Smart Code Explainer
    *Powered by Groq & Llama Models*
    """)
    
    with gr.Row():
        with gr.Column(scale=3):
            with gr.Group():
                gr.Markdown("### 📝 Paste Your Code")
                code_input = gr.Code(
                label="",
                language=None,
                interactive=True,
                lines=15,
                elem_classes="code-input"
                    )

            with gr.Row():
                expertise_toggle = gr.Radio(
                    choices=["beginner", "expert"],
                    value="beginner",
                    label="Audience Level",
                    info="Choose explanation type",
                    elem_id="expertise-radio",
                    interactive=True
                )
                model_selector = gr.Dropdown(
                    SUPPORTED_MODELS,
                    value=SUPPORTED_MODELS[0],
                    label="AI Model",
                    info="Select analysis engine",
                    interactive=True
                )
            
            with gr.Row():
                clear_btn = gr.Button("Clear", variant="secondary")
                submit_btn = gr.Button("Analyze Code →", variant="primary", size="lg")

        with gr.Column(scale=4):
            gr.Markdown("### 📖 Explanation")
            explanation_output = gr.Markdown(
                label="",
                elem_classes="explanation-output"
            )
            with gr.Group(visible=False) as error_box:
                gr.Markdown("### ❗ Error")
                error_output = gr.Textbox(label="", interactive=False)

    with gr.Accordion("📚 Example Code Snippets", open=False):
        examples = gr.Examples(
            examples=[
                ["def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a+b", "beginner"],
                ["const debounce = (fn, delay) => {\n  let timeout;\n  return (...args) => {\n    clearTimeout(timeout);\n    timeout = setTimeout(() => fn(...args), delay);\n  };\n};", "expert"],
                ["import numpy as np\n\narr = np.array([[1,2],[3,4]])\nprint(arr.T @ arr)", "beginner"],
                ["// Java example\npublic class Main {\n  public static void main(String[] args) {\n    System.out.println(\"Hello World\");\n  }\n}", "beginner"],
                ["# Ruby example\n(1..20).each do |i|\n  puts i if i % 15 == 0 ? 'FizzBuzz' : i % 3 == 0 ? 'Fizz' : i % 5 == 0 ? 'Buzz' : i\nend", "expert"]
            ],
            inputs=[code_input, expertise_toggle],
            label="Click any example to load"
        )

    # Style customizations
        demo.css = """
/* Code input styling */
.code-input textarea { 
    font-family: 'Fira Code', monospace !important;
    font-size: 14px !important;
    border: 1px solid #ddd !important;
    border-radius: 8px;
    padding: 12px;
    background-color: #fefefe;
}

/* Explanation output container */
.explanation-output { 
    background-color: #f4f6f8;
    padding: 24px;
    border-radius: 12px;
    border: 1px solid #ddd;
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    line-height: 1.6;
    color: #333;
    min-height: 300px;
    white-space: pre-wrap;
    overflow-x: auto;
}

/* Audience level radio button group */
#expertise-radio .gr-radio-group { 
    display: flex;
    gap: 1rem;
    justify-content: flex-start;
    padding: 4px;
}

#expertise-radio .gr-radio-item {
    padding: 10px 18px;
    border-radius: 8px;
    border: 1px solid #ccc;
    cursor: pointer;
    background-color: #fafafa;
    transition: all 0.2s ease-in-out;
}

#expertise-radio .gr-radio-item:hover {
    background-color: #eaeaea;
}

/* Dark mode adjustments */
.dark #expertise-radio .gr-radio-item {
    border-color: #555;
    background-color: #333;
    color: #eee;
}

.dark .explanation-output {
    background-color: #222;
    color: #ddd;
    border-color: #444;
}

.dark .code-input textarea {
    background-color: #111;
    color: #eee;
    border-color: #444 !important;
}

/* Button hover effects */
button {
    transition: background-color 0.2s ease-in-out;
}

button:hover {
    opacity: 0.9;
}
"""


    # Event handlers
    clear_btn.click(
        fn=lambda: ("", ""),
        inputs=[],
        outputs=[code_input, explanation_output]
    )
    
    submit_btn.click(
        fn=explain_code,
        inputs=[code_input, expertise_toggle, model_selector],
        outputs=explanation_output
    )

if __name__ == "__main__":
    demo.launch(server_port=7860, share=False)