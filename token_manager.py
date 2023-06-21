from re import search

def populate_db():
    db = {}
    with open("cookies.txt", "r") as f:
        for line in f.readlines():
            id, token = line.strip("\n").split(":")
            db[id] = token
    return db

def update_db(id, token):
    with open("cookies.txt", "a") as f:
        f.write(f"{id}:{token}\n")

def remove_from_db(id):
    with open("cookies.txt", 'r') as f:
        lines = f.readlines()

    lines = [line for line in lines if id not in line]
    if lines[-1][-1] != '\n':
        lines[-1] += '\n'
    with open("cookies.txt", 'w') as f:
        f.writelines(lines)

def sanitize_token(token):
    ltoken = search(r'(ltoken=[^;]+;)', token)
    ltuid = search(r'(ltuid=[^;]+;)', token)

    if ltoken and ltuid:
        ltoken = ltoken.group(1)
        ltuid = ltuid.group(1)

        return ltoken + ltuid
    else:
        return False
        
if __name__ == "__main__":
    cookies_db = populate_db()
    print(sanitize_token('ltoken=; ltuid=;'))
    print(cookies_db)
    remove_from_db('437070416780066817')
