import requests
import pandas as pd


word_entry = {}
list_of_definitions = []

while True:
    try:
        word = input(f'Please enter the word you would like to search: \n').lower()
        request = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        request_output = request.json()[0]
        meanings = request_output['meanings']
        for item in meanings:
            word_entry['word'] = word.capitalize()
            word_entry['part_of_speech'] = item['partOfSpeech'].strip()
            word_entry['meaning'] = item['definitions'][0].get('definition','')        
            word_entry['example'] = item['definitions'][0].get('example','')
            word_entry['synonym'] = item['definitions'][0].get('synonym','')
            word_entry['antonym'] = item['definitions'][0].get('antonym','')
            list_of_definitions.append(word_entry.copy())
        break  
    except:
        print('There was something wrong with your entry. Please make sure the spelling of the word is correct')


df = pd.DataFrame.from_dict(list_of_definitions)


list_of_parts_of_speech = df['part_of_speech'].tolist()
while True:
    try:
        part_of_speech_input = input(f'Please enter the part of speech you would like a meaning for: ({",".join(df["part_of_speech"].tolist())})\n').lower().strip()
        if part_of_speech_input in list_of_parts_of_speech:
            pos_df = df[df['part_of_speech'] == part_of_speech_input]
            print(pos_df)
            break
    except:
        print('There was something wrong with your entry.')
        
try:
    to_csv = input('Would you like to convert the definitions to a csv file?(Y/N)\n').lower()
    if to_csv == 'y':
        df.to_csv(f'definitions_of_{word}.csv',index=False,encoding='utf-16')
except:
    print('Sorry, there was something wrong with your entry')
print(df)
    