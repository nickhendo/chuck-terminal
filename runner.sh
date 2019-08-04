parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1 ; pwd -P )

cd "$parent_path" || exit 1
sqlite3 quotes.db "SELECT quote FROM quotes WHERE rowid=(SELECT rowid FROM quotes ORDER BY rowid limit 1)" | cowsay
sqlite3 quotes.db "DELETE FROM quotes WHERE rowid=(SELECT rowid FROM quotes ORDER BY rowid limit 1)"
python3 ./runner.py & >/dev/null
