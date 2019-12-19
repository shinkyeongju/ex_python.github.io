list_1 = [17,92,18,33,58,5,33,42]
sel = [18,33,900]
loc = []
def findNumIndex():
	for i in list_1:
		for j in sel:
			if i == j :
				if list_1.index(i) not in loc:
					loc.append(list_1.index(i))
	tkinter.messagebox.askokcancel('위치구하기', f'해당값의 위치는 {loc}')