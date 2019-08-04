# chuck_terminal
## Goal:
On opening a new terminal, show a Chuck Norris quote piped through Cowsay from https://api.chucknorris.io/jokes/random

### Phase one:
Initially this was done through adding `curl https://api.chucknorris.io/jokes/random | jq .value | cowsay` to the .bashrc. There is a lag in querying the API though, so creating a database of quotes, where one is 'popped' each time and new ones are added, seems like the right way to go. 

### Phase two:
The goal now, is to add a single line to the .bashrc, sourcing chuck_terminal which will then take care of this.

The program flow should then be:
1. Open a new terminal
2. Bashrc calls pops the oldest quote from the database
3. The script then calls a python script and backgrounds it, the script checks the database (sqlite3) to ensure it has around 10 quotes available, and adds new ones when necessary. 
