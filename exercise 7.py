import datetime
meresgia10xronia = [];
tday = datetime.date.today()
tdelta = datetime.timedelta(days=365)
currentyear = (tday.year)
ekastotexronia = tday
count = 0
print "Shmera exoume ",tday

for x in range(0, 10):
	meresgia10xronia.insert(x,ekastotexronia.isoweekday())
	if (currentyear % 4) == 0:
		if (currentyear % 100) == 0:
			if (currentyear % 400) == 0:
				tdelta = datetime.timedelta(days= 365 +1)
			else:
				tdelta = datetime.timedelta(days= 365)
		else:
			tdelta = datetime.timedelta(days=365 +1)
	else:
		tdelta= datetime.timedelta(days= 365)


	currentyear += 1
	ekastotexronia += tdelta


for x in range(1, 10):
	if meresgia10xronia[0] == meresgia10xronia[x] :
		count += 1

thesh = tday.day
mhnas = tday.month

print "Tha uparksoun " , count , "mera/es ta epomena 10 xronia pou tha einai oi" , thesh ,"es tou " , mhnas ,"ou mhna "