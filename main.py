from pyscript import display, document

def add_mmber (e) : 
    document.getElementById('output1').innerHTML = ""

    members= {'Deandre Faiyaz','Samantha Bautista', 'Chloe Adlawan', 'Julia Bermudez'}

    input_member = document.getElementById('input1', 'input2').value

    new_member = {input_member}

    all_member = members | new_member
    
    total_member = len(members | new_member)

    member_list = "<br>".join(sorted(all_mmber))

    document.getElementById('output1').innerHTML = f'All members: <br>{member_list}'
    display(f'Total members: {total_member}', target="output1")