from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str):
    """Searches for LinkedIn Page."""
    search = TavilySearchResults(include_domains=["linkedin.com"])
    res = search.run(f"{name}")
    return res
