from pyscript import document

def signup(event=None):
    #gets selected/checked items from html
    registrationyes= document.getElementById("registrationyes").checked
    medicalyes= document.getElementById("medicalyes").checked
    grade= document.getElementById("grade").value
    section= document.getElementById("section").value

    output= document.getElementById("output")
    image= document.getElementById("teamImage")
    image.style.display= "none"

    #mediacl and registration checking if done
    if not registrationyes:
        output.innerText= "Please complete the online registration first."
        return

    if not medicalyes:
        output.innerText= "Please secure a medical clearance."
        return

    #this determines the team you have
    if (
        (grade=="7" and section=="ruby") or
        (grade=="8" and section=="emerald") or
        (grade=="9" and section=="sapphire") or
        (grade=="10" and section=="sapphire")
    ):
        team="Yellow Tigers"
        img="images/tigers.png"

    elif (
        (grade=="7" and section=="sapphire") or
        (grade=="8" and section=="ruby") or
        (grade=="9" and section=="topaz") or
        (grade=="10" and section=="emerald")
    ):
        team="Red Bulldogs"
        img= "images/bulldogs.png"

    elif (
        (grade=="7" and section=="emerald") or
        (grade=="8" and section=="topaz") or
        (grade=="8" and section=="jade") or
        (grade=="9" and section=="ruby") or
        (grade=="10" and section=="topaz")
    ):
        team="Blue Bears"
        img="images/bears.png"

    else:
        team="Green Hornets"
        img="images/hornets.png"

    #output message
    message = "Congrats! You successfully joined the Intrams.\n"
    message += "Your assigned team is: " + team

    output.innerText = message
    image.src = img
    image.style.display = "block"