import csv
import os


datas = []
string = "<br>"
for filename in os.listdir('/root/L1_singapore'):
        if filename.endswith('.ovpn'):
          with open(os.path.join('/root/L1_singapore', filename)) as f:
            contents = f.readlines();
            contentStr = '\n'.join([line.strip() + string for line in contents])
            datas.append(['L1_singapore1',1,'simple-ovpn','red',contentStr])
            print(contentStr)

header = ['ovpn-name','ovpn-level','ovpn-type','ovpn-theme-color','ovpn-content']


with open('ovpn.csv','w', encoding='UTF8') as f:

        writer = csv.writer(f)

        writer.writerow(header)


        for data in datas:
          writer.writerow(data)

f.close()