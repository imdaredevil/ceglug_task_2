import csv
FN=["id","Name","Rotten","Price"]
i = -1
lis=[];
dele=[]
with open("number.csv","r") as csvf:
 read = csv.reader(csvf);
 for idx in list(read)[0]:
  i = i + 1;
  d={};
  if(idx is ""):
   if(i%2 is 0):
    dele.append(i);
   else:
    d['id']=i;
  else:
   d['id']=int(idx);
  if(len(d.keys())>0):
   lis.append(d);
i=-1
with open("fruits.csv","r") as csvf:
 read = csv.reader(csvf);
 for name in list(read)[0]:
  i=i +1;
  if i not in dele:
   for d in lis:
    if d['id'] is i:
     d['Name']=name;
 for d in lis:
  if d['Name'] is "":
   d['Name']=lis[d['id']-9]['Name']     
i=-1
with open("rotten.csv","r") as csvf:
 read = csv.reader(csvf);
 for check in list(read)[0]:
  i=i+1;
  for d in lis:
   if d['id'] is i:
    if check is "0":
     check = "f";
    elif check is "1":
     check = "t";
    if check is "t":
     d['Price'] = 0.00000
    d['Rotten'] = check
i = -1
with open("price.csv","r") as csvf:
 read = csv.reader(csvf)
 for cost in list(read)[0]:
  i = i + 1;
  for d in lis:
   if(d['id']== i):
    if(cost == ""):
     cost = 0.00000
    else:
     cost = float(cost)
    d['Price'] = cost

with open("data.csv","w") as csfv:
  write=csv.DictWriter(csvf,fieldnames=FN);
  write.writeheader();
  for d in lis:
   write.writerow(d);
with open("number.csv","w") as csvf:
  write = csv.writer(csvf)
  write.writerow([d['id'] for d in lis])
with open("fruits.csv","w") as csvf:
  write = csv.writer(csvf)
  write.writerow([d['Name'] for d in lis])
with open("price.csv","w") as csvf:
  write = csv.writer(csvf)
  write.writerow([d['Price'] for d in lis])
with open("rotten.csv","w") as csvf:
  write = csv.writer(csvf)
  write.writerow([d['Rotten'] for d in lis])
	 
