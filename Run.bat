pytest -v -s -p no:warnings --html=HtmlReports/Poonam_01111.html -=alluredir="AllureReports"

pytest -v -s -p no:warnings --html=HtmlReports/Poonam_01111.html --alluredir="AllureReports" -n=4 -m ddtparams

pytest -v -s -p no:warnings --html=HtmlReports/Poonam_01111.html --alluredir="AllureReports" -m ddtexcel
