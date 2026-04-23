# This python will be used to track my .py projects.
weeks = [[
    "Simple conversation",
    "Trial conversation",
    "Simple 2-constant calculator",
    "Replayable 2-constant calculator",
    "Assignment time estimator",
    "Simple tip calculator",
    "Calculator with return",
    "Simple structured calculator",
    "Simple inside voice converter",
    "Simple word counter",
    "Master Challenge - Einstein's Formatter"
], [
    "Simple odd or even checker",
    "10-item Quiz",
    "Simple color sorter",
    "Game recommender",
    "Master Challenge - Hitchhiker's Digital Cafe"
], [
    "Calculator or match",
    "Simple fruit dictionary",
    "Lists and dictionaries",
    "Simple word slicer",
    "Master Challenge - LRT-2 Digital Commuter Hub" 
], [
    "Better calculator",
    "Simple fruit guesser",
    "Master Challenge - Balikbayan Logistics"
], [
    "Randomized number or fruit guesser",
    "Simple red or blue guesser",
    "Simple Dragon Ball Z character API lookup"
    "Master Challenge - Digital Traveller"
]]

print("\nFull Project List")

for eachweek in range(len(weeks)):
    print(f"\nWeek {eachweek}:")
    for eachproject in range(len(weeks[eachweek])):
        print(f"{eachproject + 1}.", weeks[eachweek][eachproject])

print()