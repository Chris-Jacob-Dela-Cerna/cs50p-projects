# Document: This python is my 4th application of CS50P Week 1.

def ask():
    difficulty = input("Easy or Hard? ").strip().title()
    if not (difficulty == "Easy" or difficulty == "Hard"):
        print("Enter a valid difficulty. ")
    
    how_many = input("Singleplayer or Multiplayer? ").strip().title()
    if not (how_many == "Singleplayer" or how_many == "Multiplayer"):
        print("Enter a valid playstyle. ")
    
    return difficulty, how_many
    
def check_ask(difficulty, how_many):
    if difficulty == "Easy" and how_many == "Singleplayer":
        return "God of War"
    elif difficulty == "Easy" and how_many == "Multiplayer":
        return "Minecraft"
    elif difficulty == "Hard" and how_many == "Singleplayer": 
        return "Sekiro"
    elif difficulty == "Hard" and how_many == "Multiplayer":
        return "Rust"
        
def recommend(temp_game):
    print(f"You might like {temp_game}")
            
def main():
    difficulty, how_many = ask()
    temp_game = check_ask(difficulty, how_many)
    recommend(temp_game)

main()