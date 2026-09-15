import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
result=pd.read_csv("/content/content.csv",index_col=0)
# Main Menu
print("Main Menu")
print("1. Fetch data")
print("2. Dataframe Statistics")
print("3. Display Records")
print("4. Working on Records")
print("5. Working on Columns")
print("6. Search specific row/column")
print("7. Data Visualization")
print("8. Data analytics")
print("9. Exit")
ch=int(input("Enter your choice"))
if ch==1:
  print(result)
elif ch==2:
 while (True):
  print("Dataframe Statistics Menu")
  print("1. Display the Transpose")
  print("2. Display all column names")
  print("3. Display the indexes")
  print("4. Display the shape")
  print("5. Display the dimension")
  print("6. Display the data types of all columns")
  print("7. Display the size")
  print("8. Exit")
  ch2=int(input("Enter choice"))
  if ch2==1:
    print(result.T)
  elif ch2==2:
    print(result.columns)
  elif ch2==3:
    print(result.index)
  elif ch2==4:
    print(result.shape)
  elif ch2==5:
    print(result.ndim)
  elif ch2==6:
    print(result.dtypes)
  elif ch2==7:
    print(result.size)
  elif ch2==8:
    break
  elif ch==3:
    while(True):
      print("Display Records Menu")
      print("1. Top 5 Records")
      print("2. Bottom 5 Records")
      print("3. Specific number of records from the top")
      print("4. Specific number of records from the bottom")
      print("5. Details of a Content Type")
      print("6. Display details of all contents")
      print("7. Exit")
      ch3=int(input("Enter choice"))
      if ch3==1:
        print(result.head())
      elif ch3==2:
        print(result.tail())
      elif ch3==3:
        n=int(input("Enter how many records you want to display from the top"))
        print(result.head(n))
      elif ch3==4:
        n=int(input("Enter how many records you want to display from the bottom"))
        print(result.tail(n))
      elif ch3==5:
        st=input("Enter the content type name for which you want to see the details")
        print(result.loc[result['content_type'] == st])
      elif ch3==6:
        print("AI Generated vs Human Written Content")
        print(result)
      elif ch3==7:
         break
elif ch==4:
  while(True):
    print("Working on Records Menu")
    print("1. Insert a new record")
    print("2. Delete a specific record")
    print("3. Update a specific record")
    print("4. Exit")
    ch4=int(input("Enter choice"))
    if ch4==1:
      a=input("Enter the written or generated text here:")
      b=input("Enter content type:")
      c=int(input("Enter word count:"))
      d=int(input("Enter character count:"))
      e=int(input("Enter sentence count"))
      result.loc[a]=[b,c,d,e]
      print("Data successfully inserted")
    elif ch4==2:
      a=input("Enter index of record whose data needs to be deleted")
      result.drop(index=a,inplace=True)
      print("Data successfully deleted")
    elif ch4==3:
      a=input("Enter index of record whose data needs to be updated")
      b=input("Enter content type:")
      c=int(input("Enter word count:"))
      d=int(input("Enter character count:"))
      e=int(input("Enter sentence count"))
      result.loc[a]=[b,c,d,e]
      print("Data successfully updated")
    elif ch4==4:
      break
elif ch==5:
  while(True):
    print("Working on Columns Menu")
    print("1. Insert a new column data")
    print("2. Delete a specific column")
    print("3. Exit")
    ch5=int(input("Enter choice"))
    if ch5==1:
      print("Enter details")
      h=input("Enter column/heading name")
      det=eval(input("Enter details corresponding to all records (enclosed in [ ]):"))
      result[h]=pd.Series(data=det,index=result.index)
      print("Column inserted")
    elif ch5==2:
      a=input("Enter column name which needs to be deleted")
      result.drop([a],axis=1,inplace=False)
      print("Column Temporary deleted")
    elif ch5==3:
        break
elif ch==6:
  while(True):
    print("Search Menu")
    print("1. Search for the details of a specific record")
    print("2. Search details of a specific district as per a specific column heading")
    print("3. Exit")
    ch6=int(input("Enter choice"))
    if ch6==1:
      st=input("Enter the index of the record whose details you want to see")
      print(result.loc[st])
    elif ch6==2:
      col=input("Enter column/heading name whose details you want to see")
      print(result[col])
    elif ch6==3:
        break
elif ch==7:
  while(True):
    print("Data Visualization Menu")
    print("1. Line Plot")
    print("2. Vertical Bar Plot")
    print("3. Horizontal Bar Plot")
    print("4. Exit")
    ch7=int(input("Enter choice"))
    if ch7==1:
      while(True):
        print("Line Plot Sub Menu")
        print("1. Content type wise word count")
        print("2. Content type wise flesch_reading_ease")
        print("3. Content type wise character count")
        print("4. Exit")
        chline=int(input("Enter choice"))
        if chline==1:
          plt.figure(1)
          plt.plot(result[result['label']==1]['content_type'],result[result['label']==1]['word_count'],label="Number of Words AI")
          plt.figure(2)
          plt.plot(result[result['label']==0]['content_type'],result[result['label']==0]['word_count'],label="Number of Words Human")
          plt.title("Content Type Wise Word Count")
          plt.xlabel("Content Type")
          plt.ylabel("Word Count")
          plt.xticks(rotation=30)
          plt.legend()
          plt.grid(True)
          plt.show()
        elif chline==2:
          plt.figure(1)
          plt.plot(result[result['label']==1]['content_type'],result[result['label']==1]['flesch_reading_ease'],label="Flesch Reading Scale AI")
          plt.figure(2)
          plt.plot(result[result['label']==0]['content_type'],result[result['label']==0]['flesch_reading_ease'],label="Flesch Reading Scale Human")
          plt.title("ContentType Wise Flesch Reading Scale Ease")
          plt.xlabel("Content Type")
          plt.ylabel("Flesch Reading Scale")
          plt.xticks(rotation=30)
          plt.legend()
          plt.grid(True)
          plt.show()
        elif chline==3:
          plt.figure(1)
          plt.plot(result[result['label']==1]['content_type'],result[result['label']==1]['character_count'], label="Number of Characters AI")
          plt.figure(2)
          plt.plot(result[result['label']==0]['content_type'],result[result['label']==0]['character_count'], label="Number of Characters Human")
          plt.title("Content Type Wise Character Count")
          plt.xlabel("Content Type")
          plt.ylabel("Character Count")
          plt.xticks(rotation=30)
          plt.legend()
          plt.grid(True)
          plt.show()
        elif chline==4:
            break
    elif ch7==2:
      while(True):
        print("Vertical Bar Plot Sub Menu")
        print("1. Content type wise sentence count")
        print("2. Content type wise lexical diversity")
        print("3. Content type wise average sentence length")
        print("4. Exit")
        chbar=int(input("Enter choice"))
        if chbar==1:
          plt.figure(1)          plt.bar(result[result['label']==1]['content_type'],result[result['label']==1]['sentence_count'],label="Number of sentences AI",color="green")
          plt.figure(2)          plt.bar(result[result['label']==0]['content_type'],result[result['label']==0]['sentence_count'],label="Number of sentences Human",color="green")
          plt.title("Content Type wise Sentence Count")
          plt.xlabel("Content Type")
          plt.ylabel("Sentence Count")
          plt.xticks(rotation=30)
          plt.legend()
          plt.grid(True)
          plt.show()
        elif chbar==2:
          plt.figure(1)          plt.bar(result[result['label']==1]['content_type'],result[result['label']==1]['lexical_diversity'],label="Lexical Diversity AI",color="yellow")
          plt.figure(2)          plt.bar(result[result['label']==0]['content_type'],result[result['label']==0]['lexical_diversity'],label="Lexical Diversity Human",color="yellow")
          plt.title("Content Type wise Lexical Diversity")
          plt.xlabel("Content Type")
          plt.ylabel("Lexical Diversity")
          plt.xticks(rotation=30)
          plt.legend()
          plt.grid(True)
          plt.show()
        elif chbar==3:
          plt.figure(1)          plt.bar(result[result['label']==1]['content_type'],result[result['label']==1]['avg_sentence_length'],label="Average Sentence Length AI",color="orange")
          plt.figure(2)          plt.bar(result[result['label']==0]['content_type'],result[result['label']==0]['avg_sentence_length'],label="Average Sentence Length Human",color="orange")
          plt.title("Content Type wise Average Sentence Length")
          plt.xlabel("Content Type")
          plt.ylabel("Average Sentence Length")
          plt.xticks(rotation=30)
          plt.legend()
          plt.grid(True)
          plt.show()
        elif chbar==4:
          break
    elif ch7==3:
      while(True):
            print("Horizontal Bar Plot Sub Menu")
            print("1. Content Type wise Punctuation Ratio")
            print("2. Content Type wise Sentiment Score")
            print("3. Exit")
            chbar=int(input("Enter choice"))
            if chbar==1:
              plt.figure(1)              plt.barh(result[result['label']==1]['content_type'],result[result['label']==1]['punctuation_ratio'],label="Ratio of Punctuation AI",color="green")
              plt.figure(2)              plt.barh(result[result['label']==0]['content_type'],result[result['label']==0]['punctuation_ratio'],label="Ratio of Punctuation Human",color="green")
              plt.title("Content Type wise Punctuation Rasio")
              plt.ylabel("Content Type")
              plt.xlabel("Punctuation Ratio")
              plt.legend()
              plt.show()
            elif chbar==2:
              plt.figure(1)              plt.barh(result[result['label']==1]['content_type'],result[result['label']==1]['sentiment_score'],label="Sentiment Score AI",color="yellow")
              plt.figure(2)            plt.barh(result[result['label']==0]['content_type'],result[result['label']==0]['sentiment_score'],label="Sentiment Score Human",color="yellow")
              plt.title("Content Type wise Sentiment Score")
              plt.xlabel("Sentiment Score")
              plt.ylabel("Content Type")
              plt.xticks(rotation=30)
              plt.legend()
              plt.grid(True)
              plt.show()
            elif chbar==3:
              break
    elif ch7==4:
      break
elif ch==8:
  while(True):
        print("Data Analytics Menu")
        print("1. AI content type with maximum number of words")
        print("2. AI content type with minimum number of words ")
        print("3. Content type with maximum number of AI content")
        print("4. Human content type with minimum number of words")
        print("5. Human content type with maximum number of words")
        print("6. Content type with maximum number of Human content")
        print("7. Exit")
        ch8=int(input("Enter choice:"))
        if ch8==1:
          m=result[result['label']==1]['word_count'].max()
          s=result.loc[result['word_count']==m]
          print("AI content type with maximum number of words",m," is\n ",s.index)
        elif ch8==2:
          m=result[result['label']==1]['word_count'].min()
          s=result.loc[result['word_count']==m]
          print("AI content type with minimum number of words",m," is\n ",s.index)
        elif ch8==3:
          m=result[result['label']==1]['content_type'].value_counts().max() s=result[result['label']==1]['content_type'].value_counts()[result[result['label']==1]['content_type'].value_counts()==m].index
          print("Content type with maximum number of AI content",m," is\n ",s)
        elif ch8==4:
          m=result[result['label']==0]['word_count'].max()
          s=result.loc[result['word_count']==m]
          print("Human content type with minimum number of words",m," is\n ",s.index)
        elif ch8==5:
          m=result[result['label']==0]['word_count'].min()
          s=result.loc[result['word_count']==m]
          print("Human content type with maximum number of words",m,"is\n ",s.index)
        elif ch8==6:
          m=result[result['label']==0]['content_type'].value_counts().max()  s=result[result['label']==0]['content_type'].value_counts()[result[result['label']==0]['content_type'].value_counts()==m].index
          print("Content type with maximum number of Human content",m,"is\n ",s)
        elif ch8==7:
          break

