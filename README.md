# Text Processor

## Install & Run

1. Clone this repository
```sh
# clone project
git clone git@github.com:kraspy/string_proccessor.git

# go into dir
cd string_proccessor
```

2. Install requirements & activate venv
```sh
# Use uv
uv sync

# Use pip
pip install -r requirements.txt

# Activate venv
source .venv/bin/activate
```

3. Run streamlit-application
```sh
streamlit run app.py
```

## Available Methods

### Case Transform
- [v] Convert all letters to uppercase
- [v] Convert all letters to lowercase
- [v] Capitalize the first character of the text
- [v] Capitalize the first letter of each word
- [v] Swap the case of all letters