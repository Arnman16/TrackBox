function getPersonJSON(id) {
    $(demo).fadeOut(0);
    return new Promise(resolve => {
        $.ajax({
            type: "GET",
            url: "/vue/api/Person/" + id + "/",
            data: {},
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            success: function (data) {
                resolve(data);
                $(demo).fadeIn(300);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                console.log("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
            },
        });
    });
}
async function PersonJsonAsync(id) {
    try {
        var first_name = '';
        var last_name = '';
        var location = '';
        var result = await getPersonJSON(id)
        console.log('this')
        console.log(result);
        first_name = result.first_name;
        last_name = result.last_name;
        location = result.location;
        id = result.id;
        window.history.pushState("object or string", "Title", "/vue/person/" + id + "/");
        document.querySelector("#demo").style.visibility = 'visible';
        document.querySelector("#list").style.visibility = 'hidden';
        document.getElementById('first_name').innerHTML = first_name;
        document.getElementById('last_name').innerHTML = last_name;
        document.getElementById('location').innerHTML = location;


    } catch (error) {
        console.log('Error:', error);
    }
}