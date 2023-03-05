import requests
import tkinter as tk

session = requests.Session()

def fetch_user_data():
    email = email_entry.get()
    url = f"https://www.duolingo.com/2017-06-30/users?email={email}"

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
        'Host': "www.duolingo.com"
    }
    
    response = session.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()

        users_number = len(data['users'])
        user_id = data['users'][0]['id']
        username = data['users'][0]['username']
        bio = data['users'][0]['bio']
        hasFacebookId = data['users'][0]['hasFacebookId']
        hasGoogleId = data['users'][0]['hasGoogleId']
        fromLanguage = data['users'][0]['fromLanguage']
        hasRecentActivity15 = data['users'][0]['hasRecentActivity15']
        profileCountry = data['users'][0]['profileCountry']
        currentCourseId = data['users'][0]['currentCourseId']
        hasPhoneNumber = data['users'][0]['hasPhoneNumber']
        creationDate = data['users'][0]['creationDate']
        achievements = data['users'][0]['achievements']
        emailVerified = data['users'][0]['emailVerified']
        numbers_courses = len(data['users'][0]['courses'])

        output_label.config(text=f"""
            Users Find : {users_number}
            User ID: {user_id}
            Username: {username}
            Bio: {bio}
            Language: {fromLanguage}
            Creation Date: {creationDate}
            FacebookId: {hasFacebookId}
            GoogleId: {hasGoogleId}
            Active: {hasRecentActivity15}
            Profile Country: {profileCountry}
            Current Course ID: {currentCourseId}
            Phone Number: {hasPhoneNumber}
            Email: {emailVerified}
            Achievements: {achievements}
            Numbers of Courses: {numbers_courses}
        """)
    else:
        output_label.config(text=f"Error: {response.status_code}")

# Create the GUI
root = tk.Tk()
root.title("Duolingo User Lookup")

# Create the form
form_frame = tk.Frame(root)
form_frame.pack(padx=10, pady=10)

email_label = tk.Label(form_frame, text="Email:")
email_label.grid(row=0, column=0, sticky="w")

email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=0, column=1, padx=5)

lookup_button = tk.Button(form_frame, text="Lookup", command=fetch_user_data)
lookup_button.grid(row=1, column=1, pady=10)

# Create the output
output_frame = tk.Frame(root)
output_frame.pack(padx=10, pady=10)

output_label = tk.Label(output_frame, text="")
output_label.pack()

# Start the GUI
root.mainloop()
