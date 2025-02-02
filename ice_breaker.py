import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

from third_parties.linkedin import scrape_linkedin_profile


def main():
    load_dotenv()

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
    linkedin_data = scrape_linkedin_profile("", True)
    res = chain.invoke(input={"information": linkedin_data})
    print(res)


if __name__ == "__main__":
    main()
