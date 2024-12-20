from llama_cpp import Llama

# Load Llama model
llm = Llama(
    model_path='models/Falcon3-Mamba-7B-Base-q3_k_m.gguf',
    chat_format="chatml-function-calling",
    n_gpu_layers=-1,
    verbose=False
)

# System Message: Setting the assistant's personality
SYSTEM_MESSAGE = """
You are a virtual banking assistant. You help customers carry out various banking activities like balance inquiries, fund transfers, bill payments, and checking account history.
You can call functions with appropriate input when necessary.
"""


def ask_llm(question, functions, tool_choice=None):
    """Communicates with the LLM to process user input and call tools."""
    return llm.create_chat_completion(
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": question}
        ],
        tools=functions,
        tool_choice={"type": "function", "function": {"name": tool_choice}} if tool_choice else None
    )
