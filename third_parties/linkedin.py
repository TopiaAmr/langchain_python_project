import os
import pprint
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False) -> object:
    """
    Scrape a LinkedIn profile and return the data as a dictionary.

    Args:
        linkedin_profile_url (str): The URL of the LinkedIn profile to scrape.
        mock (bool): Whether to return a mock response for testing purposes. Defaults to False.

    Returns:
        dict: A dictionary containing the scraped data.
    """

    # If mock is True, return a mock response for testing purposes.
    # The mock response is a JSON file hosted on GitHub Gist.

    if mock:
        profile_data = (
            requests.get(
                "https://gist.githubusercontent.com/TopiaAmr/b77c0ab3bbabc3c36ad377d666cc8c0f/raw/eace51ab65bf93d035099d832d12f7077074a6b8/topia-amr-linkedin.json",
                timeout=10,
            )
            .json()
            .get("person")
        )

    else:
        # If mock is False, make a GET request to the Scrapin API endpoint.
        # The API endpoint takes two parameters:
        #   - apikey: the API key for your Scrapin account.
        #   - linkedInUrl: the URL of the LinkedIn profile to scrape.
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        res = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )
        # The API endpoint returns a JSON response.
        # The person key in the JSON response contains the scraped data.
        profile_data = res.json().get("person")

    # Filter out empty values and the certifications key which is not supported
    # by Scrapin.

    profile_data = {
        k: v
        for k, v in profile_data.items()
        # The following values are considered empty and are filtered out
        if v not in ([], "", "", None)
        # The certifications key is not supported by Scrapin and is filtered out
        and k not in ["certifications"]
    }
    # Return the filtered dictionary
    return profile_data


if __name__ == "__main__":
    data = scrape_linkedin_profile("https://eg.linkedin.com/in/topiaamr", True)
    pprint.pprint(data)
