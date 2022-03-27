To run this. Just run the main.py file with python.
I do have an exe version of this where you just run the main.exe file. You don't need python with that version.
Exe version: https://mega.nz/folder/UyBjECqD#uYj4b3gD-GTmM6x3EfnTSA

First select which image you would like to use and then the locaion the txt file will be saved.
Then simply click generate
The other settings are for fine tuning

Images do have a max size but dont worry, you do not have to resize it yourself. If an image is too large it will simply shrink it.
If you want to overide that change the dimension setting to whatever you want, however large. It will slow down though.

Basic explanation
This program first takes your settings in via the buttons and junk and sends it to the algorithm file
The algorithm takes in the settings.
Then it gets the image you have chosen and makes a copy to the internal code and makes it black and white.
It then sets it to some of the right sizing junk.

Then it looks at the image in 2 wide and 3 tall chunks.
It makes that chunk into a binary number (Look at the code notes for more info on how thats organized)

Then it uses the unicode assigned to that number (Technically i add like 10k to the number because the braille unicode is that high)

Then once it has turned those 2 by 3 letters into that braille letter. It adds it to an array for that chunk row.
It then moves over right and repeats that algorithm for that row of the image.
Then it moves down and does the same.
Left to right. Top to bottom.

Then once we have an array of arrays (basically a matrix)
I just print them to the txt doccument and open the doccument.
