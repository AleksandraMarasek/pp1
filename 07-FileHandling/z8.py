file = open('countries.txt','r') #otwieramy plik i przypisujemy go do zmiennej
file_content=file.read() #'file' zostaje zmienną na której będziemy wykonywać komendy dt. pliku który otworzyliśmy
print(file_content) #wyświetlenie zawartości pliku
file.close() #zamknięcie które trzeba zrobić za każdym razem

#??