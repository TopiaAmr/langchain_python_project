# LearnLangchain

## Description
A Langchain-powered tool that analyzes LinkedIn profiles to generate:
- Short professional summaries
- Interesting personal facts
- Technical skill insights

## Key Features
- LinkedIn profile lookup by name
- Profile data scraping
- AI-powered analysis using Ollama's mistral model

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LearnLangchain.git
   ```
2. Navigate to the project directory:
   ```bash
   cd LearnLangchain
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. Create `.env` file:
   ```bash
   echo OLLAMA_BASE_URL='http://localhost:11434' > .env
   ```

## Usage
Run the `ice_breaker.py` script to start the application:
```bash
python ice_breaker.py \
  "Amr E. Flutter App Developer Aljeraisy HR Company"
```

## Dependencies
```text
langchain
langchain-ollama
python-dotenv
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.
PRs welcome! Maintain consistent code style with:
- Type hints
- Google-style docstrings
- PEP8 formatting

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.