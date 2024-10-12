from .pdf_reader import PDFReader  # Import the PDFReader class

TOOLS = {
    "pdf_reader": PDFReader,
}

def load_tools(tool_name: str):
    if tool_name not in TOOLS:
        raise NotImplementedError(f"Tool '{tool_name}' is not implemented.")
    return TOOLS[tool_name]
