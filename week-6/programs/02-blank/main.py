
lines = [
    "I",
    "need",
    "more",
    "time.",
]

with open("phrase.txt", "w") as wrt, open("phrase.txt", "a") as add:
    wrt.write("Phrase down below:")
    for line in lines:
        add.write(line)