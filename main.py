import time
from plyer import notification
if __name__ == "__main__":
 	while True:
 		notification.notify(
 			title = "**Please Drink Water Now",
 			message = "Pls Drink Water",
 			timeout = 15,
 		)
 		time.sleep(60*60)
