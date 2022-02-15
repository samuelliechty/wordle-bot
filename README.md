Welcome to my attempt at a Wordle bot


This bot (currently) plays exclusively in hard mode and uses slightly different rules than the "hard mode" actually present in Wordle.

In Wordle's "hard mode" you're still allowed to use letters that were blacked-out but this bot doesn't do that.

This bot will also never guess a word that "wastes" a yellow tile (if the second letter was yellow in the first guess it won't try that letter there in the second guess)


CURRENT FUNCTIONALITY:

    -Play an instant game with the bot: Feed it the day's answer and it will tell you how many tries it took and what it's guesses were).

    -Play using your choice of grading type: There are three "grading" algorithms the bot can use and the user can choose between them.

    -Run analytics on one or all grading types: Only useful if you have time to let it run and are using a good IDE.

    -Custom dictionary: If you rewrite "better_tailored_dictionary.txt" you can run the bot using your own currated list of words.



PLANNED FUNCTIONALITY:

    -The ability to play "with" the bot: The bot guesses a letter, you feed the guess to Wordle, you tell the bot what the colors were, repeat.

    -More grading types: Currently there are three available grading types, two unique and one "mixed". In the future I plan to make one more unique grading type.

    -Integration with web app: Currently you can only play via a console so eventually I want to make it better to interact with.

    -Faster: The bot is kinda slow right now if you choose to run the analysis. Would love to make this faster eventually.