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
        let flip =false;
        let value =document.getElementById('search').value

        for(var i=0;i<url.length;i++){
            if('?' == url[i]){
                flip =true;
                break;
            }
        }

        if(flip) url+= ('&'+'search'+'='+value)
        else     url+= ('?'+'search'+'='+value)

    }

    else if(event == 'left' || event == 'right'){
        let flip =false;
        
        let value =document.getElementById('page_number').innerText
        
        if(event == 'left') value = parseInt(value)-1
        else value = parseInt(value)+1

        for(var i=0;i<url.length;i++){
            if('?' == url[i]){
                flip =true;
                break;
            }
        }

        if(flip) url+= ('&'+'page'+'='+value)
        else     url+= ('?'+'page'+'='+value)

    }
    else{
        let flip =false;
        let name = event.target.name;
        let value = event.target.value;
        value = value.replace(/ /g, '+')

        for(var i=0;i<(url).length;i++){
            if('?' == url[i]){
                flip =true;
                break;
            }    
        }

        if(flip) url+= ('&'+name+'='+value)
        else     url+= ('?'+name+'='+value)
    
    }
    console.log(url)
    customFetch(url,"GET")
}