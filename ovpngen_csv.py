import csv
import os


datas = []
string = "<br>"
for filename in os.listdir('/root/xxxx'):
        if filename.endswith('.ovpn'):
          with open(os.path.join('/root/xxxx', filename)) as f:
            contents = f.readlines();
            contentStr = '\n'.join([line.strip() + string for line in contents])
            datas.append(['xxxx','NORMAL','country','xxxURL',contentStr,'red', 1 ])
            print(contentStr)

header = ['OVPN_name','OVPN_type','OVPN_country','OVPN_COUNTRY_FLAG_IMG_URL','OVPN_content','OVPN_theme_color','OVPN_level']


with open('ovpn.csv','w', encoding='UTF8') as f:

        writer = csv.writer(f)

        writer.writerow(header)


        for data in datas:
          writer.writerow(data)

f.close()
