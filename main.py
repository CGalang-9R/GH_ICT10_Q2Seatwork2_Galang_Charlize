from pyscript import display, document

def gwa(e):
    document.getElementById('final').innerHTML=""
    document.getElementById('Ffinal').innerHTML=""
    firstname = document.getElementById('Fname').value
    lastname = document.getElementById('Lname').value
    eng = float(document.getElementById('english').value)
    math = float(document.getElementById('maths').value)
    filo = float(document.getElementById('filipino').value)
    ss = float(document.getElementById('socialstudies').value)
    sci = float(document.getElementById('science').value)
    ict = float(document.getElementById('icts').value)
    Lsubjs = ['eng', 'math', 'filo', 'ss', 'sci', 'ict']
    Tsubjs = (5, 5, 3, 3, 5, 2)
    sum = eng + math + filo + ss + ict + sci
    average = sum / len(Lsubjs)

    grades = f'''
    Name: {firstname} {lastname}

    English: {eng}
    Math: {math}
    Filipino: {filo}
    Social Studies: {ss}
    Science: {sci} 
    ICT: {ict}'''
    
    display (grades, target='final')

    display(f'General Weighted Average: {average:.2f}', target='Ffinal')
