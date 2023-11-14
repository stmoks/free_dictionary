### Dictionary

The program is meant to emulate a basic dictionary or search engine. I used the Free Dictionary API along with pandas to create terminal functionality for searching a word's definition and the particular part of speech should the word have multiple meanings.

#### Additional Notes

- When adding dictionary items to a list, we need to use the copy method with every iteration to move the data
- The get method can be used to search for dictionary keys without getting an error, regardless of whether the key exists
- Ensure that the encoding can handle all relevant strings for the use case - in this case, utf-8 was not appropriate
