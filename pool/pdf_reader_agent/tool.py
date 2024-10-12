from typing import AnyStr, Optional, Type
from pydantic import BaseModel, Field
from gentopia.tools.basetool import BaseTool
import PyPDF2
import requests

class PDFReaderArgs(BaseModel):
    url: str = Field(..., description="The URL of the PDF to read.")

class PDFReader(BaseTool):
    """Tool for reading PDF content from a given URL."""

    name = "pdf_reader"
    description = ("Reads and extracts text content from a PDF file located at the given URL.")

    args_schema: Optional[Type[BaseModel]] = PDFReaderArgs

    def _run(self, url: AnyStr) -> str:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        with open('temp.pdf', 'wb') as f:
            f.write(response.content)

        with open('temp.pdf', 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
        return text

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    pdf_url = "https://arxiv.org/pdf/2407.02067"
    print(PDFReader()._run(pdf_url))

