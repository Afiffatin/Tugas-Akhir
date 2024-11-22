#calc.py
class Kalkulator:
	
	# Constructor
	def __init__(self, bb, tb, usia, gender, akt):
		self.bb = bb
		self.tb = tb
		self.usia = usia
		self.gender = gender
		self.akt = akt
		self.kalori = 0
		
	# Pengihitung kalori	
	def bmr(self):
		pria = (88362 + (13397 * self.bb) + (4799 * self.tb) - (5677 * self.usia)) * (10 ** -3)
		wanita = (447593 + (9247 * self.bb) + (3098 * self.tb) - (4330 * self.usia)) * (10 ** -3)
		if self.gender == "pria":
			bmr = pria
		elif self.gender == "wanita":
			bmr = wanita
		koef = {
			1: 1.2,
			2: 1.375,
			3: 1.55,
			4: 1.725,
			5: 1.9,
		}
		koef_kalori = koef.get(self.akt)
		self.kalori = bmr * koef_kalori
		self.kalori = round(self.kalori, 1)
		return self.kalori
	
	# Penghitung jumlah protein per berat badan
	def protein(self):
		koef = {
			1: 0.8,
			2: 0.975,
			3: 1.15,
			4: 1.325,
			5: 1.5,
		}
		koef_protein = koef.get(self.akt)
		kali_protein = koef_protein * self.bb
		protein = round(kali_protein, 1)
		return protein
	
    # Penghitung jumlah lemak per kalori    
	def lemak(self):
		jml_lemak = 0.35 * self.kalori
		lemak_consume = jml_lemak / 9
		lemak = round(lemak_consume, 1)
		return lemak
	
	# Penghitung jumlah karbohidrat per kalori
	def karbo(self):
		jml_karbo = 0.65 * self.kalori
		karbo_consume = jml_karbo / 4
		karbo = round(karbo_consume, 1)
		return karbo
	
	# Penghitung jumlah gula yang bisa dikonsumsi per hari
	def gula(self):
		gula = (self.kalori / 10) / 4
		gula = round(gula, 1)
		return gula
		
# Penguji file
if __name__ == "__main__":
	bb = 50
	tb = 170
	usia = 18
	gender = "pria"
	akt = 2
	
	tingkat = {
     1: "sangat ringan",
     2: "ringan",
     3: "sedang",
     4: "aktif",
     5: "sangat aktif"
    }
	aktivitas = tingkat.get(akt)
    
	tes = Kalkulator(bb, tb, usia, gender, akt)
	kalori = tes.bmr()
	kalori = round(kalori)
	protein = tes.protein()
	lemak = tes.lemak()
	karbo = tes.karbo()
	
	print(f"Berat: {bb} kg\nTinggi: {tb} cm\nUsia: {usia} tahun\nGender: {gender}\nAktivitas fisik: {aktivitas}\n\n")
	print(f"BMR: {kalori} kkal\nProtein: {protein} gram\nLemak: {lemak} gram\nKarbo: {karbo} gram")
