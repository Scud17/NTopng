import requests
import time


session = requests.Session()


def get_data():
    dataFile = open("CSC495Data.txt", "a")
    ntopng_web_interface = session.get('http://localhost:3000', auth=('admin', 'CSC495!!'))
    ip_cam = session.get('https://www.insecam.org/en/view/436650/')
    json_page = session.get('http://127.0.0.1:3000/lua/host_get_json.lua?ifid=0&host=187.170.90.179', auth=('admin',
                                                                                                            'CSC495!!'))
    data = json_page.json()
    dataFile.write(str(data["throughput_bps"]))
    dataFile.write("\n")

    print(data["throughput_bps"])


dataFile = open("CSC495Data.txt", "a")
t_end = time.time() + 60 * 120  # run for x amount of minutes
while time.time() < t_end:
    get_data()
    time.sleep(10)

print("Data collection completed")

