import PyPDF2
from pathlib import Path

# PDF failu adrese
adrese = Path("C:/Users/User/Desktop/GAZES Rekini")
rekini = list(adrese.glob("*.pdf"))

# Vērtības
pilna_cena = 0
count = 0

# Visu PDF failu atvēršana izmantojot ciklu
for fails in rekini:
    with open(fails, "rb") as pdf:
        pdf_fails = PyPDF2.PdfReader(pdf)
        lpp_skaits = len(pdf_fails.pages)

        # No PDF dokumenta lapaspusēm tiek nolasītas vērtības
        for lpp in range(min(1, lpp_skaits)):
            page = pdf_fails.pages[lpp]
            text = page.extract_text()

            # Nosaka pozīciju tekstā kur atrodās nepieciešamā informācija ar rēķina datiem
            pos1 = text.find("Summa samaksai *:")
            pos2 = text.find(".Samaksas termiņš")
            
            # Tiek pārbaudīts vai pozīcijas eksistē PDF failā, nolasa nepieciešamos datus no PDF
            summa_text = text[pos1 + len("Summa samaksai *:"):pos2-12].strip()

            # Pārveido no String vērtības uz Float vērtību
            summa_float = float(summa_text.replace(" €", ""))
                    
            pilna_cena += summa_float
            count += 1
                

# Veic nepieciešamos aprēķinus lai noskaidrotu vidējo un pilno cenu par visiem mēnešiem kopā
if count > 0:
    average_summa = pilna_cena / count
    print(f"Pilna cena: {round(pilna_cena, 1)} €")
    print(f"Vidēja cena: {round(average_summa, 1)} €")
else:
    print("Kļūda")



