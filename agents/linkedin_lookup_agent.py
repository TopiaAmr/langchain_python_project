import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub

from tools.tools import get_profile_url_tavily

load_dotenv()


def lookup(name: str, mock: bool = False) -> str:
    if mock:
        return "https://www.linkedin.com/in/topiaamr/"

    llm = ChatOllama(
        model="mistral",
        temperature=0,
        base_url=os.getenv("OLLAMA_BASE_URL"),
        num_ctx=8000,
    )
    template = """given the full name {name_of_person} I want you to get me a link to their Linkedin profile page. 
    Your answer only contain only a URL without formatting or wrapping around quotes."""

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"],
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google for Linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt,
    )
    agent_exec = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True,
    )
    result = agent_exec.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)},
    )
    return result["output"]


if __name__ == "__main__":
    url = lookup("Amr E. Flutter App Developer Aljeraisy HR Company")
    print(url)
