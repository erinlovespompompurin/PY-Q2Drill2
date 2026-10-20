from pyscript import display, document

def add_member (e) : 
    document.getElementById('output1').innerHTML = ""

    members= 
    grade_7= {'Deandre Faiyaz'}
    grade_8= {'Samantha Bautista'}
    grade_9= {'Deandre Faiyaz'}
    grade_10= {'Deandre Faiyaz'}

    input_member = document.getElementById('input1').value
    input_member2 = document.getElementById('input2').value

    new_member = {input_member + " " + input_member2}

    all_member = members | new_member
    
    total_member = len(members | new_member)

    member_list = "<br>".join(sorted(all_member))

    document.getElementById('output1').innerHTML = f'All members: <br>{member_list}'
    display(f'Total members: {total_member}', target="output1")