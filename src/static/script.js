// append row to the HTML table
$(document).ready(() => {

    $('#myTableHeader').each(function(){
        $(this).append(`<td>1</td>`);
        $(this).append(`<td>2</td>`);
        $(this).append(`<td>3</td>`);
    })

    $('#addColumnChild').click(function(){
        $('#myTable tr').each(function(){
          $(this).append(`<td><input></input></td>`);
        })

        $('#myTableHeader').each(function(){
            $(this).append('<td>' + ($('#myTableHeader td').length + 1) + '</td>');
        })
    });
    
    $('#addRowChild').click(function(){
        $('#myTable tbody').append(`<tr>${$('#default-row').html()}</tr>`);
    });

    $('#removeRow').click(function(){
        if ($('#myTable tr').length === 1){
            console.log("I never delete my last friend!!!!!");
        }else{
            $('tr:last-child').closest('tr').remove();
        }
        
    });

    $('#removeColumn').click(function(){
        if ($('#myTable td').length === 1){
            console.log("I never delete my last friend!!!!!");
        }else{
            $("#myTable th:last-child, #myTable td:last-child").remove();
        }
    });

    $('#sendData').click(function(){
        $("#download-button").children().remove()
        sendData()
    });

    

})

async function getTableToWeb(){
    const url = '/table/0&4&3';
    var responseTable = document.getElementById('myTable');

    const fetchOptions = {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
        },
    };

    const res = await fetch(url, fetchOptions);    
    const ret = await res.json();
    console.log(ret.poorTable);
         
     //Get data to table
    for (r = 0; r < ret.poorTable.length; r++){
        responseTable.insertRow(responseTable.rows.length)
        for(s = 0; s < ret.poorTable[0].length; s++){
            var input = document.createElement("input")
            var cell = responseTable.rows[r].insertCell(s)
            var div = document.createTextNode(input);
            cell.appendChild(div)
        }
    }  
}

async function sendData() {
    var myRows = [];
    var tbody = document.getElementById("myTableBody");
    var tWarning = document.getElementById("warning-text");
    
    for (i = 0; i < tbody.rows.length; i++) {
        var dict = {}
        for (j = 0; j < tbody.rows[0].cells.length; j++){
            if (tbody.rows[i].cells[j].childNodes[0].value != ""){
                dict[j] = tbody.rows[i].cells[j].childNodes[0].value;
            }
        }
        if (Object.keys(dict).length !== 0){
            myRows.push(dict);
        }
    }

    var dict = {
        "data": myRows
      }

    const myJSON = JSON.stringify(dict);
    var responseTable = document.getElementById('responseTableBody');
    responseTable.textContent = '';
    
    if(myJSON.length <= 2){
        return responseTable.innerHTML = "Body is empty!!!";        
    }

    const url = '/getInformation';
    const fetchOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
        },
    body: myJSON
    };

    const res = await fetch(url, fetchOptions);

    try{
        const ret = await res.json();
        tWarning.innerHTML = ""
        console.log(ret.length)
        //Get data to table
        console.log(ret.length)
        for (r = 0; r < ret.length; r++){
            console.log("prvni c");
            responseTable.insertRow(responseTable.rows.length)
            for(s = 0; s < ret[0].length; s++){
                var value = ret[r][s];

                var cell = responseTable.rows[r].insertCell(s)
                var div = document.createTextNode(value);
                cell.appendChild(div)
            }
            n_r = r+1
            var nameRows = "TC" + n_r.toString()
            var cellName = responseTable.rows[r].insertCell(0)
            var divNameCell = document.createTextNode(nameRows)
            cellName.appendChild(divNameCell)
        }  

        const excelDivButton = document.getElementById("download-button")
        
        let newDiv = document.createElement("div");
        const newSpan = document.createElement("span");
        newDiv.className = "download-button"
        newDiv.id = "download-response-excel"
        newDiv.addEventListener("click", download)
        newSpan.textContent = "Download"
        newDiv.appendChild(newSpan)
        excelDivButton.appendChild(newDiv)


    } catch (error){
        return tWarning.innerHTML = "We dont have orthogonal table which can works on your parameters."
    }
}

// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
    } else { 
      x.className = x.className.replace(" w3-show", "");
    }
  }

function download(){
    $("#responseTable").table2excel({
        filename: "data_to_excel.xls"
    });
}