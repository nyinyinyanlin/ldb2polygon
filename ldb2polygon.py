def convert(file):
	ll = None
	tmp_poly = []
	polys = []
	with open(file,"r") as f:
		lines = f.readlines()
	for line in lines:
		line = line.rstrip()
		if len(line) >= 0:
			if line.startswith("B"):
				ll = "poly"
				if len(tmp_poly) > 0:
					polys.append(tmp_poly)
				tmp_poly = []
				print(line)
			elif ll == "poly":
				ll = "meta"
			elif ll == "meta":
				point = line.split(" ")
				print(point)
				if len(point) == 2:
					point = [float(point[0]),float(point[1])]
					tmp_poly.append(point)
	if len(tmp_poly) > 0:
		polys.append(tmp_poly)
	return polys
