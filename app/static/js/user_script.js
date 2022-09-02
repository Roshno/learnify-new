var url_tag = document.getElementById("url");
var url =url_tag.innerText;

function customFetch(url,type,data){

    if(type== "GET"){
        fetch(url,{
            mehtod: type
        })
        .then( res => {
            if(res.ok){
                console.log("GET Successfull")
            }
        })
    }
    else if(type == "POST"){
        fetch(url,{
            mehtod: type,
            header: {
                "Content-type": "application/json"
            },
            body : JSON.stringify(data)
        })
        .then( res => {
            if(res.ok){
                console.log("POST Successfull")
            }
        })
    }
}

function redisplay(event){

    if(event === "search"){
        let value =document.getElementById('search').value
        url+= ('?search='+value)
        alert(url)
        customFetch(url,"GET")
    }
    else{
        
        let name = event.target.name;
        let value = event.target.value;
        url+= ('?'+name+'='+value)
        alert(url)
        customFetch(url,"GET")
    }
}