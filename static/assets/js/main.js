function login(){
    var user, pass;
    user = document.getElementById("user").value;
    pass = document.getElementById("password").value;

    if(user=="Miguel" && pass=="1234"){
        window.location = "file:///C:/J-Travel/Proyecto-Ciclo3-J-Travel/J-Travel-Vista/index.html";
    }
}