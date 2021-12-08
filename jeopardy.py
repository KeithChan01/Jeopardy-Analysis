import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('jeopardy.csv')
df.rename(columns = {
    'Show Number' : 'show_number',
    ' Air Date' : 'air_date',
    ' Round' : 'round',
    ' Category' : 'category',
    ' Value' : 'value',
    ' Question' : 'question',
    ' Answer' : 'answer'
}, inplace = True)

print(df.head())

def filter_questions(data, words):
    # Lowercases all words in the list of words as well as the questions. Returns true if all of the words in the list appear in the question.
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  # Applies the labmda function to the question column and returns the rows where the function returns True
  return data.loc[data['question'].apply(filter)]

filtered = filter_questions(df, ['King', 'England'])
print(filtered['question'].head())

df['float_value'] = df['value'].apply(lambda x: float(x[1:].replace(',','') if x != 'None' else 0))

king_float_value = filter_questions(df,['King'])
print(king_float_value.mean())

def unique_answers(data):
  return king_float_value['answer'].value_counts()
print(unique_answers(king_float_value))
  
