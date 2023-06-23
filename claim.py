import subprocess

def check_in(token):
    logs = subprocess.getstatusoutput(f'hoyo-daily-logins-helper --cookie="{token}" --starrail')[1].split("\n")
    for line in logs:
        if "Already" in line:
            return "Already checked in for today!"

    cleaned_output = [entry.split(':')[-1].strip('\t') for entry in logs][3:7]
    return cleaned_output

if __name__ == "__main__":
    print(check_in("Test"))

