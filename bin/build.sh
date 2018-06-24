cd ..
rm -f mainApp.spec
rm -fr build
rm -fr dist
activenv timaster35
pyinstaller --onefile \
    --add-binary ./content/delete.png:content \
    src/mainApp.py