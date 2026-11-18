
import pandas as pd

# read the orginal csv file
df = pd.read_csv("video_games_raw.csv")

print("VIDEO GAME CATALOG MANAGER")
print()

# Ask user what row they want to look at
row_number = int(input("Enter a row number to inspect: "))

# check if the row actually exists
if row_number < 0 or row_number >= len(df):
    print("Invalid row number.")

else:
    # get the selected game using iloc
    game = df.iloc[row_number]

    print()
    print("Selected Game:")
    print("Title:", game["Title"])
    print("Platform:", game["Platform"])
    print("Genre:", game["Genre"])
    print("Rating:", game["Rating"])
    print("Current Status:", game["Status"])

    # ask for the new game status
    print()
    new_status = input("Enter a new status: ")

    # update the status for that specifc game
    row_label = df.index[row_number]
    df.at[row_label, "Status"] = new_status

    # add a new column for recomended games
    df["Recommended"] = "No"

    # use loc to update games that meet both requirments
    df.loc[
        (df["Rating"] >= 8) & (df["Price"] <= 40),
        "Recommended"
    ] = "Yes"

    # find all the recommended games using query
    recommended_games = df.query("Recommended == 'Yes'")

    print()
    print("Recommended Games:")
    print(recommended_games[["Title", "Platform", "Price", "Rating"]])

    # save everything to a new csv so original isnt changed
    df.to_csv("video_games_cleaned.csv", index=False)

    print()
    print("The catalog has been updated.")
    print("Saved as video_games_cleaned.csv.")
