
function onClick(){
    const first_name=document.getElementById("first_name").value;
    const last_name=document.getElementById("last_name").value;
    const email=document.getElementById("email").value;
    console.log(first_name, last_name, email)
    axios.post('add_student', {'first_name':first_name, 'last_name':last_name, 'email':email})
    .then((response =>(console.log(response))))
}