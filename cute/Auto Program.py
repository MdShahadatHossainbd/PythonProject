
import webbrowser as wb

def webauto():
    # path your computer where chrome path
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'#ADD THE PATH OF CHROME HERE
    URLS = (
        	"stackoverflow.com",
	        "https://github.com/MdShahadatHossainbd",
	        "gmail.com",
	        "google.com",
	        "youtube.com"
    )
    for url in URLS:
        print("opening :"+ url)
        wb.get(chrome_path).open(url)

webauto()