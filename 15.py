# 

def ask():
    difficulty = input("Easy or Hard? ").strip().title()
    how_many = input("Singleplayer or Multiplayer? ")
    return difficulty, how_many

def check_ask(difficulty, how_many):
    if difficulty == "Easy":
        if how_many == "Singleplayer":
            return "God of War"
        elif how_many == "Multiplayer":
            return "Minecraft"
        else:
            return "None"
    elif difficulty == "Hard":
        if how_many == "Singleplayer":
            return "Sekiro"
        elif how_many == "Multiplayer":
            return "Rust"
        else:
            return "None"
    else:
        return "None"

def recommend(temp_game):
    print(f"You might like {temp_game}")
            

def main():
    difficulty, how_many = ask()
    temp_game = check_ask(difficulty, how_many)
    recommend(temp_game)

main()