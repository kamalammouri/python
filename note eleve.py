eleve= [{'nom':'Karim','note':13.4}, {'nom':'Ahmed', 'note':12}, {'nom':'Salim', 'note':10},
{'nom':'Meriem', 'note':15}, {'nom':'Hanan', 'note':9.5}]


def classer(data):
    def get_note(e):
        return e.get('note')
    data=data.sort(key=get_note, reverse=True)
    return data
    

print(classer(eleve))
