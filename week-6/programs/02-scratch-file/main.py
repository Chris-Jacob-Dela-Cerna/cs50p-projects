# i/o scratch file - practicing txt and csv file handling

lines = [
    "I",
    "need",
    "more",
    "time.",
]

with open("phrase.txt", "w") as wrt:
    wrt.write("Phrase down below: \n")

with open("phrase.txt", "a", newline="\n") as add:
    for line in lines:
        add.writelines(line + "\n")