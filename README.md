Here's a professional README.md for your Code Explainer application:

```markdown
# 🚀 Smart Code Explainer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

An AI-powered code explanation tool that helps developers understand code snippets at different expertise levels, powered by Groq and Llama models.

## Features ✨

- **Multi-Language Support** - Works with any programming language
- **Adaptive Explanations** - Choose between beginner-friendly or expert-level analysis
- **AI Model Selection** - Switch between different Llama models
- **Code Examples** - Built-in examples for quick testing
- **Responsive Design** - Clean UI with dark/light mode support
- **Syntax Highlighting** - Automatic language detection and formatting

## Installation 🛠️

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/code-explainer.git
cd code-explainer
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

## Usage 🖥️

1. **Start the application**
```bash
python app.py
```

2. **Open in browser**
```
http://localhost:7860
```

3. **Interface Guide**
- 📝 Paste code into the input area
- 🎚 Select expertise level (Beginner/Expert)
- 🤖 Choose AI model (Llama 3-70B or Llama 2-70B)
- 🚀 Click "Analyze Code" for explanation

## Configuration ⚙️

### Supported Models
- `llama-3.3-70b-versatile` (Default)
- `llama2-70b-4096`

### Environment Variables
```env
GROQ_API_KEY=your_groq_api_key
```

### Server Settings
```python
demo.launch(
    server_port=7860,  # Default port
    share=False       # Set to True for public sharing
)
```

## Examples 📚

```python
# Fibonacci Sequence
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
```

```javascript
// Debounce Function
const debounce = (fn, delay) => {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => fn(...args), delay);
  };
};
```

## Dependencies 📦

- Python 3.8+
- gradio
- python-dotenv
- requests

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** Ensure you have valid API credentials from [Groq](https://groq.com/) before using this application. API usage may be subject to Groq's terms of service.
```
