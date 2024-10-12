### Define your custom tool here. Check prebuilts in gentopia.tool (:###
from typing import AnyStr, Optional, Type
from googlesearch import search
from pydantic import BaseModel, Field
from gentopia.tools.basetool import BaseTool

class GoogleSearchArgs(BaseModel):
    query: str = Field(..., description="A search query")

class GoogleSearch(BaseTool):
    """Tool that adds the capability to query the Google search API."""

    name = "google_search"
    description = ("A search engine retrieving top search results as snippets from Google. "
                   "Input should be a search query.")

    args_schema: Optional[Type[BaseModel]] = GoogleSearchArgs

    def _run(self, query: AnyStr) -> str:
        """Run a Google search and return the top search results."""
        results = search(query, num=5)  # Get top 5 search results
        return '\n\n'.join([str(item) for item in results])

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        """Asynchronous run method, currently not implemented."""
        raise NotImplementedError

if __name__ == "__main__":
    # Example usage of the GoogleSearch tool
    google_search_tool = GoogleSearch()
    search_results = google_search_tool._run("Attention for transformer")
    print(search_results)
