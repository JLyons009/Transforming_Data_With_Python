import read


data = read.load_data()

def remove_sub(domain):
    split_domain = str(domain).split('.')
    if len(split_domain) == 3:
        return split_domain[1] + '.' + split_domain[2]
    elif len(split_domain) == 2:
        return split_domain[0] + '.' + split_domain[1]
    else:
        return split_domain[0]

domains = data['url'].apply(remove_sub).value_counts().head(100)

if __name__ == "__main__":
    for name, row in domains.items():
        print('{0}: {1}'.format(name, row))