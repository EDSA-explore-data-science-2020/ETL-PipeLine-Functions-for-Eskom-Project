
import pandas as pd
import numpy as np

#-----------------includes----------------
# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}




# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former',
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to',
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still',
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose',
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take',
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind',
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next',
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor',
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least',
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call',
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves',
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others',
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody',
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten',
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty',
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too',
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon',
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me',
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}



#----------------------functions-------------

### START FUNCTION 1
def dictionary_of_metrics(items):
    """ dictionary_of_metrics(items)
    
        Returns a dict with keys 'mean', 'median', 'var', 'std', 'var', 'min', and 'max'.

        Parameters:
        -----------
        (list): electrification by province - gauteng data

        Return:
        -------
        (dict): dictionary of  mean, median, variance, standard deviation, minimum and maximum
    """

    items_sorted = sorted(items)
    mean = np.mean(items_sorted)
    median = np.median(items_sorted)
    minimum = np.min(items_sorted)
    maximum = np.max(items_sorted)
    std = np.std(items_sorted, ddof=1)
    variance = np.var(items_sorted, ddof=1)


    return {'mean': round(mean,2), 'median': round(median,2), 'var': round(variance, 2), 'std': round(std,2), 'min': round(minimum,2), 'max': round(maximum,2)}

### END FUNCTION 1


### START FUNCTION 2
def five_num_summary(items):
    """ five_num_summary(items)
    
        Returns a dict with keys 'max', 'median', 'min', 'q1', and 'q2'.

        Parameters:
        -----------
        (list): electrification by province - gauteng data

        Return:
        -------
        (dict): dictionary of  'max', 'median', 'min', 'q1', and 'q2'.
    """
    items_sorted = sorted(items)

    maximum = np.max(items_sorted)
    minimum = np.min(items_sorted)
    median = np.median(items_sorted)
    q1 = np.percentile(items_sorted,25)
    q3 = np.percentile(items_sorted,75)

    summary = {'max': maximum, 'median': median, 'min': minimum, 'q1': q1, 'q3': q3}
    return summary

### END FUNCTION 2


### START FUNCTION 3
def date_parser(dates):
    """date_parser(dates)

      Return a list of Date strings.

      Parameters
      ----------
      (list): list of datetime strings (REQUIRED)

      Return
      ------
      (list): list of Date strings.

      Examples
      -------
      >>>dates = ['2019-11-29 12:50:54',
         '2019-11-29 12:46:53',
         '2019-11-29 12:46:10',
         '2019-11-29 12:33:36',
         '2019-11-29 12:17:43',
         '2019-11-29 11:28:40']

      >>>date_parser(dates)
      >>>['2019-11-29',
          '2019-11-29',
          '2019-11-29',
          '2019-11-29',
          '2019-11-29',
          '2019-11-29']
    """
    return [datetime.split()[0] for datetime in dates]

### END FUNCTION 3


### START FUNCTION 4
def extract_municipality_hashtags(df, mun_dict = mun_dict):
    """extract_municipality_hashtags(df)
  
    returns a modified dataframe that includes two new columns \
    that contain information about the municipality and hashtag of the tweet.

    Parameters: 
    ----------
    (pd_DataFrame) takes a pandas dataframe as input.

    Return: 
    ------
    returns a pandas dataframe as input with new columns ‘municipality’ and ‘hashtags’.
  """

  #----------municipality_match function--------
def municipality_match(string_from_series):
    municipality = np.nan     #declearing and assigning the municipality list with nan from np.nan
    for dic_key in mun_dict:               #looping through the municipality_dict dictionary and grabing one key at a time.
      if dic_key in string_from_series:             #checking if the dictionary key is in or contained within the string_from_series from the pandas series of tweets.
          municipality = mun_dict[dic_key] #loading/ appending the municipality with the value from the dictionary corresponding with the key.
          break                                     #Breaking the loop if one municipality matched or detected. 
    return municipality                             #Returning the resulting list of municipalities per tweet

  #----------hashtags_match function--------
def hashtags_match(string_from_series):
      hashtags = []         #declearing an empty list to store the hashtags
      for word in string_from_series.lower().split(' '): # spliting the received string into a list of words and looping from the list to access each word at the time!
        if word.startswith('#'):        #checking if the retrieved word starts with a #
            hashtags.append(word)       #Appending the word(hashtag) into the list hashtags 

      if len(hashtags) != 0: #Checking if the hashtags list is  Empty
          return hashtags    #Returning the hashtags list and exiting the hashtags_match function
      else:
          hashtags =np.nan   #if the hashtags list is  Empty, we assign a nan value from the numpy library!
          return hashtags

  #--------Calling and using the two functions to modify the Dataframe---------
      df['municipality'] = df['Tweets'].apply(municipality_match)       #Calling the municipality_match function using the pandas series method apply() to modify by creating the municipality column.  
      df['hashtags'] = df['Tweets'].apply(hashtags_match)         #Calling the hashtags_match function using the pandas series method apply() to modify by creating the hashtags column. 
  #-------------
      return df     #returnig the resulting dataframe with all the changes.

### END FUNCTION 4


### START FUNCTION 5
def number_of_tweets_per_day(df):
    """number_of_tweets_per_day(df)
    
    The Number of Tweets per Day Function calculates the number of tweets that were posted per day.
 
    Parameters
    ----------
    (Dataframe):  takes a pandas dataframe as input.
    
    Return
    ------
    (Dataframe): returns a new dataframe, grouped by day, with the number of tweets for that day.

    """
    # Initialise empty dataframe
    df_date_count = pd.DataFrame()
    
    # Copy dates from intial dataframe
    df_date_count['Date'] = df['Date']
    
    # Convert into datetime and only show date
    df_date_count['Date'] = pd.to_datetime(df_date_count['Date'])
    df_date_count['Date'] = df_date_count['Date'].dt.date
    
    # Count amount of dates and save to new column
    df_date_count['Tweets'] = 1
    df_date_count = df_date_count.groupby(['Date']).count()
    
    return df_date_count

### END FUNCTION 5

### START FUNCTION 6
def word_splitter(df):
    """word_splitter(df)
    
    splits the sentences in a dataframe's column into a list of the separate words.
    
    Parameters
    ----------
    (Dataframe):  takes a pandas dataframe as input.
 
    Return
    ------
    (Dataframe): returns the dataframe with a new column ‘Split Tweets’
    """
    # your code here
    df['Split Tweets'] = df['Tweets'].apply(lambda string_from_series: string_from_series.lower().split())
    
    return df

### END FUNCTION 6





### START FUNCTION 7
def stop_words_remover(df,  stop_words_dict = stop_words_dict ):
    """stop_words_remover(df)
    
    removes English stop words from a tweet.
 
    Parameters
    ----------
    (Dataframe):  takes a pandas dataframe as input.
 
    Return
    ------
    (Dataframe): returns the dataframe with a new column 'Without Stop Words'
    """
    # your code here
    def remover(string_from_serie):
      return [ word for word in string_from_serie.lower().split() if word not in stop_words_dict['stopwords']]

    df['Without Stop Words'] = df['Tweets'].apply(remover)
    
    return df

### END FUNCTION 7



