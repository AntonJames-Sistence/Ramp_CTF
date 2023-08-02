# Quick guide

## ``words.txt``

* This file contains collection of dictionary words each consist of exactly seven letters.

## ``initial_message.py`` | ``initialMessage.js``

* Both files serve the same purpose of decoding a coded message. They achieve this by utilizing built-in methods like ``atob()`` in JavaScript and ``base64`` in Python.

## ``decypher.py``

* This file is designed to handle the brute force decryption of a hashed word using a given salt. It accomplishes this by iterating through a list of words from a text file and comparing each word's hash with the input hashed word. If any matches are detected, the corresponding words are appended to the result array.

## ``dictionary.py``

* Create a user-friendly dictionary that associates letters with their corresponding values in a key-value pair format.

## ``http_request.py``

* In the first part, it efficiently handles HTTP requests by sending them and storing the responses in a results array.
* The second part processes the array of responses, extracting unique letters and leaving them for further use.
* Lastly, the third part performs a comprehensive search through the words.txt file, identifying words that contain all the unique letters gathered in the previous part.