# Word and Token Counter

This is a Streamlit app that allows users to upload a DOCX or TXT file or enter text directly into a text box. The app then counts and displays the number of words and tokens in the text.

## Features

- Upload DOCX or TXT files
- Enter text directly into a text area
- Count the number of words in the text
- Count the number of tokens in the text using the `tiktoken` library

## Installation

To run this app, you need to have Python installed. Follow the steps below to set up the app:

1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/word-token-counter.git
    cd word-token-counter
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Upload a DOCX or TXT file using the file uploader, or enter text directly into the text area.
2. The app will automatically count and display the number of words and tokens in the text.

## Files

- `app.py`: The main Streamlit app script.
- `requirements.txt`: A list of required Python packages.
- `README.md`: This file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) - Framework for creating web apps
- [tiktoken](https://github.com/openai/tiktoken) - Tokenizer library
- [python-docx](https://python-docx.readthedocs.io/en/latest/) - Library for creating and updating Microsoft Word (.docx) files

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any questions or suggestions, please open an issue or contact [yourname](mailto:yourname@example.com).

