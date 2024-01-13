![Book Creator](URL_картинки)

# Book Creator | Small but Useful Software

### Destination:
I think many preppers know that you can sell your books on Amazon, but what do you do if you're not a writer?
I offer you a solution (you only have to pay for OpenAI ChatGPT4 tokens, about ~$2 for 1 book that has 8 chapters, 5 sections each). I think that knowledgeable people will find an adaptation of this program! Success!!!


Before you start working with the program, you need to get an OpenAI API token, it can be obtained on the page https://platform.openai.com/api-keys by clicking on the button "Create a new key" (if this is your first token, you will still need to link your bank card).

Open the .env file and insert your token in the "" in the line API_TOKEN_CHAT_GPT=""

```cmd
API_TOKEN_CHAT_GPT="YOU TOKEN"
```

### Installing dependencies:
(Need python > 3.7 version)

```python
pip install -r requirements.txt
```

### Generating the book skeleton:
To generate the book skeleton you need to run this code:
(on windows just use the word python without the number 3)

```python
python3 generete.py
```

You will be prompted to enter the topic you want to write a book on, after entering, press Enter, wait. You will get a skeleton, if you are happy with the skeleton, then close this program and start creating the book.

### The creation of the book itself:
Run main.py, you will be prompted to enter a comment to generate, the first time I advise without comment, just press Enter, see how it does without your interference in the commands, if something does not suit you, you can try to play with the commands, just write, for the bot, sort of, writing the book, do not forget that you need to use this or that ...

```python
python3 main.py
```

Wait for generation to finish, it takes about 20 minutes, go make some coffee ☕️
At the end, the program will try to open the document, if you do not have Word installed on your computer, you will probably get some error from the operating system.
But the file with the generated text is in the root of the program called <b>generated_e_book.docx</b>.