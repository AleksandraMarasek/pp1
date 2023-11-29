def main():
    countries=[
    {"name": "Poland","population":38000000},
    {"name": "France","population": 123457889},
    {"name": "UK","population": 786868009},
    {"name": "Croatia","population": 12374647747},
    {"name": "Japan","population": 341300000}
    ]
    
    print(f"COUNTRY \t POPULATION")
    i=0
    while i != len(countries):
        print(f'{countries[i]["name"]:10},{countries[i]["population"]:<10}')
        i+=1

if __name__=='__main__':
    main()



