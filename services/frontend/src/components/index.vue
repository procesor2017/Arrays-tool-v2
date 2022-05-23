<template>
  <div id="app">

        <div class ="main-menu" id="main-menu">
            <ul class="topnav">
            <li><a href="#" class="main-menu-href">HOME</a></li>
            <li><a href="#guide" class="main-menu-href">Guide</a></li>
            <li><a href="#input-table" class="main-menu-href">INPUT TABLE</a></li>
            <li><a href="#result-table" class="main-menu-href">RESPONSE TABLE</a></li>
            <li><a href="https://www.tesena.com/en/contact" class="main-menu-href">CONTACT</a></li>
            <li style="float:right; padding: 0;"><a href="https://www.tesena.com/en" class="main-menu-href" style="float:right; padding: 12px; height: 100%;">
                <svg width="150px" height="40px" float="right" >       
                <image xlink:href="https://www.tesena.com/files/logo-tesena.svg" width="150px" height="40px" float="right"/>    
                </svg>
            </a></li>
            </ul>
        </div>

        <div class="main-body">
            <div class="index-div">
            
            <div class="index-div-left">
                <h1>Testing 360°</h1>
                We focus all our activities on testing.
                <a href="https://www.tesena.com/en">
                <div class="btn-radius-border">
                    EXPLORE
                </div>
                </a>
                
            </div>
            <div class="index-div-right"></div>
            </div>


            <div class="guide" id="guide">
                <h2 class="web-h2">Guide</h2>
                Orthogonal array testing is a black box testing technique that is a systematic, statistical way of software testing.
                Every column in input table has one variable with n rows, which they represent different values.

                Number of column will be same as number of variable, which we need to combine and the number of rows then corresponds to the highest number of values that any of these variables can take.
            </div>

            <div class="input-table" id="input-table">
                <h2 class="web-h2">INPUT TABLE</h2>
                <div class="button-menu-table">
                    <div id="addRowChild" class="div-menu">Add Row</div>
                    <div id="addColumnChild" class="div-menu">Add Column</div>
                    <div id="removeRow" class="div-menu">Delete Row</div>
                    <div id="removeColumn" class="div-menu">Delete Column</div>
                    <div id="sendData" class="div-menu-blue">Send Data</div>
                </div>
                <table id="myTable" class="myTable">
                    <thead id="myTableHeader">
                    </thead>
                    <tbody id="myTableBody">
                        <tr id="default-row">
                        <td><input></td>
                        <td><input></td>
                        <td><input></td>
                        </tr>
                        <tr>
                        <td><input></td>
                        <td><input></td>
                        <td><input></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="result-table" id="result-table">
                <h2>Response table</h2>
                    <table id="responseTable">
                        <tbody id="responseTableBody"></tbody>
                        <div id="warning-text"></div>
                    </table> 
                <div id="download-button"></div>
            </div>
        </div>

        <div class="footer" id="footer">
            <a href="https://www.facebook.com/tesena.smart.testing/" class="fa fa-facebook"></a>
            <a href="https://www.instagram.com/jsmetesena/?utm_medium=copy_link" class="fa fa-instagram"></a>
            <a href="https://www.youtube.com/channel/UCXAYaVsc9AocWpVzHiGXtHQ" class="fa fa-youtube"></a>
            <a href="https://www.linkedin.com/company/tesena/" class="fa fa-linkedin"></a>
        </div>

    </div>

</template>

<script>

</script>