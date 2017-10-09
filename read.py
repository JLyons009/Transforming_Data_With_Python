import pandas as pd


def load_data():    
    stories = pd.read_csv('hn_stories.csv')
    stories.columns = ['submission_time', 'upvotes', 'url', 'headline']
    if __name__ == "__main__":
        print(stories.head(10))
    return stories

if __name__ == "__main__":
    load_data()