import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()


def ice_break_with(name: str) -> str:
    linkedin_url: str = lookup(name)
    linkedin_data = scrape_linkedin_profile(linkedin_url.replace("'",""))

    summary_template = """
    given the LinkedIn information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatOllama(
        model="mistral",
        temperature=0,
        base_url=os.getenv("OLLAMA_BASE_URL"),
    )

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": linkedin_data})
    print(res)


if __name__ == "__main__":
    ice_break_with("Amr E. Flutter App Developer Aljeraisy HR Company")
