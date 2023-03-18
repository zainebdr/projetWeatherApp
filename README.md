# projetWeatherApp

to clone project 
git clone https://github.com/Mady0101/projetWeatherApp.git

working steps 
//check if you are on main 
git branch main 

// get latest updates 
git pull 

//to add new features always create new branch 
git checkout -b <your branch name>

// implement your code 
//try to make commits with minimal changes 
//for every new changes do
git add . (to add all changes) or git add <file name>
git commit -m <your message to indicate what changes you made>





// go back to main and get latest updates
git checkout main
git pull

//go back to your branch 
git checkout <your branch name>
git merge main 

// resolve conflicts if there is any 

//when you finish implementing code and resolving conflicts
git push 
// if you haven't yet added your branch to remote repo
git push --set-upstream origin <your branch name>

//create a pull request
