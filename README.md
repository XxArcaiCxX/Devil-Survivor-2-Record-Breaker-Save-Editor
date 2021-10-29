# Devil Survivor 2 Record Breaker Save Editor
This is a save editor for the 3DS game Devil Survivor 2 Record Breaker.

## Requirements:
* **Python 3** to run the program
* **3DS Running CFW** so you have access to the uncompressed save file, I recommend [JKSM](https://github.com/J-D-K/JKSM) but there are others that work fine too.

## Usage:
* Go to the directory in your SD Card where you have your save files
    * You should have 5 file that represent the 5 save slots
    * If it has 100KB of size then it's an empty save file
    * Make sure you select a non-empty save file
    
![SaveFiles](https://github.com/XxArcaiCxX/DeSu2SE/blob/main/media/DeSu2Savefiles.png?raw=true)

* Open the save file in Editor then select the tab of what you want to edit and press apply after every change
* All the skill numbers are listed on the listboxes at the bottom
* Keep in mind every value is an Integer and therefore you shouldn't use any hex (the save editor converts by itself)

## Known Issues
When you restore the save file in JKSM it may give you an error if you have empty save slots.
This is a JKSM bug, simply restart your console because the changes will still be applied. 

If you have an empty demon slot you won't be able to change it. Make sure you have demons beforehand

### Happy Editing Hee-ho
![Hee-ho](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages-wixmp-ed30a86b8c4ca887773594c2.wixmp.com%2Ff%2Fd61d9068-1085-4f27-a191-a45c02e6c921%2Fd7ma2n6-db03afbd-0542-4ec9-9865-4938866b280d.png%2Fv1%2Ffill%2Fw_205%2Ch_200%2Cstrp%2Fjack_frost_he_ho_by_flaremor_d7ma2n6-200h.png%3Ftoken%3DeyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzkyIiwicGF0aCI6IlwvZlwvZDYxZDkwNjgtMTA4NS00ZjI3LWExOTEtYTQ1YzAyZTZjOTIxXC9kN21hMm42LWRiMDNhZmJkLTA1NDItNGVjOS05ODY1LTQ5Mzg4NjZiMjgwZC5wbmciLCJ3aWR0aCI6Ijw9NDAxIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.JBZM-ah-oZOSKpB0m8dr4V-4DxCn7uhMa39bRHUuRwA&f=1&nofb=1)
