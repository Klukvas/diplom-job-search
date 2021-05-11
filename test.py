from re import search
href = "/company825/vacancy8405613"
company = search(r'company\d+', href).group(0).replace('company', '')
print(company)