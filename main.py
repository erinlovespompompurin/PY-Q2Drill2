
from pyscript import display, document

def add_member(e):
    grade_7 = {'Deandre Faiyaz'}
    grade_8 = {'Samantha Bautista'}
    grade_9 = {'Chloe Adlawan'}
    grade_10 = {'Julia Bermudez'}

    members = grade_7 | grade_8 | grade_9 | grade_10

    input_member = document.getElementById('input1').value
    input_member2 = document.getElementById('input2').value
    
    new_member = {input_member + " " + input_member2}

    all_member = members | new_member
    total_member = len(all_member)

    member_list = "<br>".join(sorted(all_member))

    document.getElementById('output1').innerHTML = (
        f"<b>Grade 7:</b> {', '.join(sorted(grade_7))}<br>"
        f"<b>Grade 8:</b> {', '.join(sorted(grade_8))}<br>"
        f"<b>Grade 9:</b> {', '.join(sorted(grade_9))}<br>"
        f"<b>Grade 10:</b> {', '.join(sorted(grade_10))}<br><br>"
        f"<b>All Members:</b><br>{member_list}<br><br>"
        f"<b>Total Members:</b> {total_member}"
    )
