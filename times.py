import read
import dateutil


data = read.load_data()

def hour(timestamp):
    time = dateutil.parser.parse(timestamp)
    return time.hour

data['hour'] = data['submission_time'].apply(hour)

if __name__ == "__main__":
    print(data['hour'].value_counts())