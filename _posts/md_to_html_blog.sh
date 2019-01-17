for f in *.md; do pandoc -t html $f -o ${f%.md}.html; done
